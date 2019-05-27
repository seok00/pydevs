#pragma once
#include "stdafx.h"
#include "Tglobal.h"
#include "atomic.h"
#include <time.h>
#include <stdlib.h>

class Mosquito : public ATOMIC {
public:
    CString JobID;
	double	ETime;
	double	LTime;
	double	PTime;
	double	ITime;
	double	DTime;
	int		ICount;
public:
	Mosquito(CString);
	Mosquito(char *);

    void ExtTransitionFN(double,DevsMessage);
	void IntTransitionFN(void);
	void OutputFN(void);
	void InitializeFN(void);
};
