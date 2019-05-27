#include "stdafx.h"
#include "genr.h"

GENR::GENR() : ATOMIC() {
	SetName("GENR");
}

GENR::GENR(CString EName) : ATOMIC(EName) {
	SetName(EName);
}

GENR::GENR(char *EName) : ATOMIC(EName) {
 	SetName(EName);
}

void GENR::ExtTransitionFN(double E, DevsMessage X){
	char GENRMessage[100]={0,}; 

	Display(Name); Display("(EXT) --> :");
	Display(X.ContentPort()); Display(": ");
	sprintf(GENRMessage,"When: %lf",AddTime(GetLastEventTime(),E));
	Display(GENRMessage);

	if (X.ContentPort() == "stop") { Passivate(); }
	else if (X.ContentPort() == "change") { Level++; }
	else if (X.ContentPort() == "set_new") {
		Level = 0;
		isDead = FALSE;
		if (Count >= 100)
			Passivate();
	}
	NewLine();
}

void GENR::IntTransitionFN(void){
	char GENRMessage[100]={0,}; 

	Display(Name); Display("(INT) --> ");
	sprintf(GENRMessage,"Sigma: %lf  When: %lf",Sigma, AddTime(GetLastEventTime(),Sigma));
	Display(GENRMessage);
	if (Phase == "busy") {
		HoldIn("busy", InterArrivalTime);
	}
	else { Passivate(); }
	NewLine();
}

void GENR::OutputFN(void){
	CString O;
	char Num[10]={0,};
	char GENRMessage[100]={0,}; 

	Display(Name); Display("(OUT) --> ");
	sprintf(GENRMessage,"Phase: %s  Sigma: %lf  When: %lf",Phase,Sigma,GetNextEventTime());
	Display(GENRMessage); NewLine();

	if (Phase == "busy" && Level == 0){
		 sprintf(Num,"%d",Count++);
		 O = "Egg-";
		 O += Num;
		 Level++;
		 MakeContent("new_egg",&O);
		 
	}
	else if (Phase == "busy" && isDead == FALSE){
		EnviPercent = rand() % 100;
		KillPercent = 50 - 10 * Level;
		if (EnviPercent < KillPercent) {
			sprintf(Num, "%d", Count-1);
			O = "Egg-";
			O += Num;
			sprintf(Num, "%d%%", KillPercent);
			O += " is Killed by ";
			O += Num;
			isDead = TRUE;
			MakeContent("attack", &O);
		}
	}
	else MakeContent();
}

void GENR::InitializeFN(void){
	Level = 0;
	InterArrivalTime = 1;
	Count = 0;
	srand((unsigned int)time(NULL));
	isDead = FALSE;

	HoldIn("busy",0.0);
}
