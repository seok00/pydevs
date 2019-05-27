#include "stdafx.h"
#include "Mosquito.h"


Mosquito::Mosquito(CString EName) : ATOMIC(EName) {
    SetName(EName); 
}

Mosquito::Mosquito(char *EName) : ATOMIC(EName)  {
    SetName(EName); 
}

void Mosquito::ExtTransitionFN(double Time, DevsMessage MSG) {
	Display(Name); Display("(EXT) --> ");
	JobID = *((CString *)(MSG.ContentValue()));
	Display(MSG.ContentPort()); Display(":"); Display(JobID);
	if (MSG.ContentPort() == "new") {
		HoldIn("egg", ETime);
	}
	else if (MSG.ContentPort() == "killed") {
		ICount = 0;
		HoldIn("dead", DTime);
	}
	else Continue();
	NewLine();
}

void Mosquito::IntTransitionFN(void) {
	Display(Name); Display("(INT) --> ");
	if (Phase == "egg") { Display("egg to larva"); HoldIn("larva", LTime); }
	else if (Phase == "larva") { Display("larva to pupa"); HoldIn("pupa", PTime); }
	else if (Phase == "pupa") { Display("pupa to imago"); HoldIn("imago", ITime); }
	else if (Phase == "imago") {
		if (ICount < 3) {
			ICount++;
			Display(JobID);
			Display(" spawn");
			if (ICount < 2)
				HoldIn("imago", ITime);
			if (ICount == 3)
				HoldIn("imago", (double)1.0);
		}
		else {
			Display(JobID);
			Display(" is dead");
			ICount = 0;
			Passivate();
		}
	}
	else if (Phase == "dead") { Passivate(); }
	else Continue();
	NewLine();
}

void Mosquito::OutputFN(void) {
	Display(Name); Display("(OUT) --> ");
	
	if (Phase == "egg") { MakeContent("trans",&JobID); }
	else if (Phase == "larva") { MakeContent("trans", &JobID); }
	else if (Phase == "pupa") { MakeContent("trans", &JobID); }
	else if (Phase == "imago") {
		if (ICount < 3) {
			CString O;
			char Num[10] = { 0, };
			sprintf(Num, "%d", rand() % 201 + 500);
			O = Num;
			MakeContent("next_egg", &O);
		}
		else {
			MakeContent("end", &JobID);
		}
	}
	else if (Phase == "dead") { MakeContent("end", &JobID); }
	else MakeContent();
}

void Mosquito::InitializeFN(void){
	ETime = (double)3.0;
	LTime = (double)7.0;
	PTime = (double)2.0;
	ITime = (double)3.0;
	DTime = (double)0.0;
	ICount = 0;
	Passivate();

	srand((unsigned int)time(NULL));
}