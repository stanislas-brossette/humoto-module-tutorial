/**
    @file
    @author  Alexander Sherikov

    @copyright 2017 INRIA. Licensed under the Apache License, Version 2.0. (see
    LICENSE or http://www.apache.org/licenses/LICENSE-2.0)

    @brief
*/


#pragma  once

namespace humoto
{
    /**
     * @brief Example: example module
     *
     * @ingroup Modules
     * @{
     * @defgroup example example
     * @}
     *
     * @ingroup example
     */
    namespace example
    {
    }
}

#include "humoto/walking.h"

#include "example/step_plan.h"
#include "tools/logger.h"
#include "example/problem_parameters.h"
#include "example/model_state.h"
#include "example/model.h"
#include "example/simple_mpc.h"
#include "example/task_com_velocity.h"
#include "example/task_cop_bounds.h"
#include "example/task_cop_pos_ref.h"
#include "example/setup_hierarchy.h"
