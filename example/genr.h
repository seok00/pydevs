#pragma once
#include "stdafx.h"
#include "Tglobal.h"
#include "atomic.h"
#include <time.h>
#include <stdlib.h>

class GENR : public ATOMIC {
public:
	int     InterArrivalTime;
//	int     ProcessingTime;
//	int     ProblemLevel;
	int     Count;
	int		Level;
	int		EnviPercent;
	int		KillPercent;
	bool	isDead;
	
public:
	GENR();
	GENR(CString);
	GENR(char *);

    void ExtTransitionFN(double,DevsMessage);
	void IntTransitionFN(void);
	void OutputFN(void);
	void InitializeFN(void);
};

