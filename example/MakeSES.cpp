#pragma once
#include "stdafx.h"
#include "Tglobal.h"
#include "Entstr.h"

#include "genr.h"
#include "Transd.h"
#include "Mosquito.h"

ENTSTR * EFP;
void MakeSES(void)
{	

	EFP = new ENTSTR("m-ef");
	EFP->AddItem(new Mosquito("Mosquito"));
	EFP->AddItem(new DIGRAPH("EF"));

	EFP->AddCouple("EF", "Mosquito", "n-n", "new");
	EFP->AddCouple("EF", "Mosquito", "a-k", "killed");
	EFP->AddCouple("Mosquito", "EF", "trans", "t-c");
	EFP->AddCouple("Mosquito", "EF", "end", "e-s");
	EFP->AddCouple("Mosquito", "EF", "next_egg", "e-g");

	EFP->SetCurrentItem("EF");
	EFP->AddItem(new GENR("Genr"));
	EFP->AddItem(new Transd("Transd"));
	EFP->AddCouple("EF", "Transd", "e-g", "next_gen");
	EFP->AddCouple("EF", "Transd", "e-s", "solved");
	EFP->AddCouple("EF", "Genr", "t-c", "change");
	EFP->AddCouple("EF", "Genr", "e-s", "set_new");

	EFP->AddCouple("Transd", "Genr", "quit", "stop");

	EFP->AddCouple("Genr", "EF", "new_egg", "n-n");
	EFP->AddCouple("Genr", "EF", "attack", "a-k");
	EFP->AddCouple("Genr", "Transd", "new_egg", "arr_egg");
	EFP->AddCouple("Genr", "Transd", "attack", "arr_attack");
}
void StartSimulation()
{
	EFP->Restart();
}