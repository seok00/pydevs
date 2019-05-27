#include "stdafx.h"
#include "transd.h"


Transd::Transd(CString EName) : ATOMIC(EName){
	  SetName(Name);
}

Transd::Transd(char *EName) : ATOMIC(EName){
	  SetName(Name);
}

void Transd::ExtTransitionFN(double E, DevsMessage X){
	 JobID = *(CString *)X.ContentValue();
	 clock += E;

	 Display(Name); Display("(EXT) --> :"); 
	 Display(X.ContentPort());
	 Display(":"); Display(JobID); 
	 Display(" at "); Display(clock);
	 NewLine();
	 if (Phase == "active"){
	     if (X.ContentPort() == "arr_egg") {
			 NewEgg.Jobs[NewEgg.Num].ID = JobID;
			 NewEgg.Jobs[NewEgg.Num].Time = clock;
			 NewEgg.Num++;
	     }
	     else if (X.ContentPort() == "arr_attack") {
			 Killed.Jobs[Killed.Num].ID = JobID;
			 Killed.Jobs[Killed.Num].Time = clock;
			 Killed.Num++;
	     }
		 else if (X.ContentPort() == "solved") {
			 Solve.Jobs[Solve.Num].ID = JobID;
			 Solve.Jobs[Solve.Num].Time = clock;
			 Solve.Num++;
		 }
		 else if (X.ContentPort() == "next_gen") {
			 NextEgg.Jobs[NextEgg.Num].ID = JobID;
			 NextEgg.Jobs[NextEgg.Num].Time = clock;
			 NextEgg.Num++;
			 totalEgg += _ttoi(JobID);
		 }
	 }
	 Continue();
}

void Transd::IntTransitionFN(void) {
	 Display(Name); Display("(INT) --> "); NewLine();

	 if (Phase == "active") {
	     PrintNewEgg();
		 PrintKilled();
		 PrintSolve();
		 PrintNextEgg();
		 Passivate();
	 }
	 else Continue();
}

void Transd::OutputFN(void) {
	 Display(Name); Display("(OUT) --> "); NewLine();
	 if (Phase == "active") 
		 MakeContent("quit",NULL);
	 else MakeContent();
}

void Transd::InitializeFN(void){
	  clock = (double)0.0;

	  NewEgg.Num = 0;
	  Killed.Num = 0;
	  Solve.Num = 0;
	  NextEgg.Num = 0;
	  totalEgg = 0;

	  HoldIn("active",(double)2200.0);
}


void Transd::PrintNewEgg(void){
	 NewLine();
     Display("   ---------------------< NewEgg Jobs >---------------------");
	 NewLine();
	 for (int i=0; i<NewEgg.Num; i++){
		 Display("("); Display(NewEgg.Jobs[i].ID);
		 Display(","); Display(NewEgg.Jobs[i].Time);
		 Display(") ");
	 }
	 NewLine();
}

void Transd::PrintKilled(void){
	NewLine();
	Display("   ---------------------< Killed Jobs >---------------------");
	NewLine();
	for (int i = 0; i<Killed.Num; i++){
		Display("("); Display(Killed.Jobs[i].ID);
		Display(","); Display(Killed.Jobs[i].Time);
		Display(") ");
	}
	NewLine();
}

void Transd::PrintSolve(void){
	 NewLine();
     Display("   ---------------------< Solved Jobs >---------------------");
	 NewLine();
	 for (int i=0; i<Solve.Num; i++){
	     Display("("); Display(Solve.Jobs[i].ID); 
		 Display(","); Display(Solve.Jobs[i].Time);
		 Display(") ");
	 }
	 NewLine();
}

void Transd::PrintNextEgg(void){
	char Num[10] = { 0, };
	sprintf(Num, "%d", totalEgg);
	NewLine();
	Display("   ---------------------< NextEgg Jobs >---------------------");
	NewLine();
	for (int i = 0; i<NextEgg.Num; i++){
		Display("("); Display(NextEgg.Jobs[i].ID);
		Display(","); Display(NextEgg.Jobs[i].Time);
		Display(") ");
	}
	NewLine();
	NewLine();
	Display("This generation's 100 eggs makes ");
	Display(Num);
	Display(" eggs in next generation!!!");
	NewLine();
}