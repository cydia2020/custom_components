import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    CONF_COMMAND,
    CONF_LAMBDA,
    CONF_MODEL,
    CONF_MULTIPLY,
    CONF_OFFSET,
    CONF_SENSORS,
    CONF_SOURCE,
    CONF_TIME,
    CONF_VERSION,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_TEMPERATURE,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_PERCENT,
    ICON_RADIATOR,
    ICON_THERMOMETER,
    ICON_TIMER,
    STATE_CLASS_MEASUREMENT,
    UNIT_CELSIUS,
    UNIT_EMPTY,
    UNIT_MINUTE,
    UNIT_PERCENT,
    UNIT_WATT_HOURS,
)
from .. import (
    vbus_ns,
    VBus,
    CONF_VBUS_ID,
    CONF_DELTASOL_C,
    CONF_DELTASOL_CS2,
    CONF_DELTASOL_BS_PLUS,
    CONF_CUSTOM,
    CONF_DEST,
)

DeltaSol_C = vbus_ns.class_('DeltaSol_C_sensor', cg.Component)
DeltaSol_CS2 = vbus_ns.class_('DeltaSol_CS2_sensor', cg.Component)
DeltaSol_BS_Plus = vbus_ns.class_('DeltaSol_BS_Plus_sensor', cg.Component)
VBusCustom = vbus_ns.class_('VBusCustom_sensor', cg.Component)

CONF_TEMPERATURE_1 = "temperature_1"
CONF_TEMPERATURE_2 = "temperature_2"
CONF_TEMPERATURE_3 = "temperature_3"
CONF_TEMPERATURE_4 = "temperature_4"
CONF_TEMPERATURE_5 = "temperature_5"
CONF_PUMP_SPEED = "pump_speed"
CONF_PUMP_SPEED_1 = "pump_speed_1"
CONF_PUMP_SPEED_2 = "pump_speed_2"
CONF_OPERATING_HOURS = "operating_hours"
CONF_OPERATING_HOURS_1 = "operating_hours_1"
CONF_OPERATING_HOURS_2 = "operating_hours_2"
CONF_HEAT_QUANTITY = "heat_quantity"

UNIT_HOUR = "h"

CONFIG_SCHEMA = cv.typed_schema(
    {
        CONF_DELTASOL_C: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(DeltaSol_C),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_TEMPERATURE_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_3): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_4): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_PUMP_SPEED_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    icon=ICON_PERCENT,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_EMPTY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_PUMP_SPEED_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    icon=ICON_PERCENT,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_EMPTY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_OPERATING_HOURS_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_HOUR,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_OPERATING_HOURS_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_HOUR,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_HEAT_QUANTITY): sensor.sensor_schema(
                    unit_of_measurement=UNIT_WATT_HOURS,
                    icon=ICON_RADIATOR,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_ENERGY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TIME): sensor.sensor_schema(
                    unit_of_measurement=UNIT_MINUTE,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                ),
            }
        ),

        CONF_DELTASOL_CS2: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(DeltaSol_CS2),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_TEMPERATURE_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_3): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_4): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_5): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_PUMP_SPEED): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    icon=ICON_PERCENT,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_EMPTY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_OPERATING_HOURS): sensor.sensor_schema(
                    unit_of_measurement=UNIT_HOUR,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_HEAT_QUANTITY): sensor.sensor_schema(
                    unit_of_measurement=UNIT_WATT_HOURS,
                    icon=ICON_RADIATOR,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_ENERGY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_VERSION): sensor.sensor_schema(
                    accuracy_decimals=2,
                    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                ),
            }
        ),

        CONF_DELTASOL_BS_PLUS: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(DeltaSol_BS_Plus),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_TEMPERATURE_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_3): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TEMPERATURE_4): sensor.sensor_schema(
                    unit_of_measurement=UNIT_CELSIUS,
                    icon=ICON_THERMOMETER,
                    accuracy_decimals=1,
                    device_class=DEVICE_CLASS_TEMPERATURE,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_PUMP_SPEED_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    icon=ICON_PERCENT,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_EMPTY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_PUMP_SPEED_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_PERCENT,
                    icon=ICON_PERCENT,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_EMPTY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_OPERATING_HOURS_1): sensor.sensor_schema(
                    unit_of_measurement=UNIT_HOUR,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_OPERATING_HOURS_2): sensor.sensor_schema(
                    unit_of_measurement=UNIT_HOUR,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_HEAT_QUANTITY): sensor.sensor_schema(
                    unit_of_measurement=UNIT_WATT_HOURS,
                    icon=ICON_RADIATOR,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_ENERGY,
                    state_class=STATE_CLASS_MEASUREMENT,
                ),
                cv.Optional(CONF_TIME): sensor.sensor_schema(
                    unit_of_measurement=UNIT_MINUTE,
                    icon=ICON_TIMER,
                    accuracy_decimals=0,
                    device_class=DEVICE_CLASS_DURATION,
                    state_class=STATE_CLASS_MEASUREMENT,
                    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                ),
                cv.Optional(CONF_VERSION): sensor.sensor_schema(
                    accuracy_decimals=2,
                    entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                ),
            }
        ),

        CONF_CUSTOM: cv.COMPONENT_SCHEMA.extend(
            {
                cv.GenerateID(): cv.declare_id(VBusCustom),
                cv.GenerateID(CONF_VBUS_ID): cv.use_id(VBus),
                cv.Optional(CONF_COMMAND): cv.uint16_t,
                cv.Optional(CONF_SOURCE): cv.uint16_t,
                cv.Optional(CONF_DEST): cv.uint16_t,
                cv.Optional(CONF_LAMBDA): cv.lambda_,
            }
        ),
    },
    key=CONF_MODEL, lower=True, space="_",
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    if config[CONF_MODEL] == CONF_DELTASOL_C:
        cg.add(var.set_command(0x0100))
        cg.add(var.set_source(0x4212))
        cg.add(var.set_dest(0x0010))
        if CONF_TEMPERATURE_1 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_1])
            cg.add(var.set_temperature1_sensor(sens))
        if CONF_TEMPERATURE_2 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_2])
            cg.add(var.set_temperature2_sensor(sens))
        if CONF_TEMPERATURE_3 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_3])
            cg.add(var.set_temperature3_sensor(sens))
        if CONF_TEMPERATURE_4 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_4])
            cg.add(var.set_temperature4_sensor(sens))
        if CONF_PUMP_SPEED_1 in config:
            sens = await sensor.new_sensor(config[CONF_PUMP_SPEED_1])
            cg.add(var.set_pump_speed1_sensor(sens))
        if CONF_PUMP_SPEED_2 in config:
            sens = await sensor.new_sensor(config[CONF_PUMP_SPEED_2])
            cg.add(var.set_pump_speed2_sensor(sens))
        if CONF_OPERATING_HOURS_1 in config:
            sens = await sensor.new_sensor(config[CONF_OPERATING_HOURS_1])
            cg.add(var.set_operating_hours1_sensor(sens))
        if CONF_OPERATING_HOURS_2 in config:
            sens = await sensor.new_sensor(config[CONF_OPERATING_HOURS_2])
            cg.add(var.set_operating_hours2_sensor(sens))
        if CONF_HEAT_QUANTITY in config:
            sens = await sensor.new_sensor(config[CONF_HEAT_QUANTITY])
            cg.add(var.set_heat_quantity_sensor(sens))
        if CONF_TIME in config:
            sens = await sensor.new_sensor(config[CONF_TIME])
            cg.add(var.set_time_sensor(sens))

    elif config[CONF_MODEL] == CONF_DELTASOL_CS2:
        cg.add(var.set_command(0x0100))
        cg.add(var.set_source(0x1121))
        cg.add(var.set_dest(0x0010))
        if CONF_TEMPERATURE_1 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_1])
            cg.add(var.set_temperature1_sensor(sens))
        if CONF_TEMPERATURE_2 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_2])
            cg.add(var.set_temperature2_sensor(sens))
        if CONF_TEMPERATURE_3 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_3])
            cg.add(var.set_temperature3_sensor(sens))
        if CONF_TEMPERATURE_4 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_4])
            cg.add(var.set_temperature4_sensor(sens))
        if CONF_TEMPERATURE_5 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_5])
            cg.add(var.set_temperature5_sensor(sens))
        if CONF_PUMP_SPEED in config:
            sens = await sensor.new_sensor(config[CONF_PUMP_SPEED])
            cg.add(var.set_pump_speed_sensor(sens))
        if CONF_OPERATING_HOURS in config:
            sens = await sensor.new_sensor(config[CONF_OPERATING_HOURS])
            cg.add(var.set_operating_hours_sensor(sens))
        if CONF_HEAT_QUANTITY in config:
            sens = await sensor.new_sensor(config[CONF_HEAT_QUANTITY])
            cg.add(var.set_heat_quantity_sensor(sens))
        if CONF_VERSION in config:
            sens = await sensor.new_sensor(config[CONF_VERSION])
            cg.add(var.set_version_sensor(sens))

    elif config[CONF_MODEL] == CONF_DELTASOL_BS_PLUS:
        cg.add(var.set_command(0x0100))
        cg.add(var.set_source(0x4221))
        cg.add(var.set_dest(0x0010))
        if CONF_TEMPERATURE_1 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_1])
            cg.add(var.set_temperature1_sensor(sens))
        if CONF_TEMPERATURE_2 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_2])
            cg.add(var.set_temperature2_sensor(sens))
        if CONF_TEMPERATURE_3 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_3])
            cg.add(var.set_temperature3_sensor(sens))
        if CONF_TEMPERATURE_4 in config:
            sens = await sensor.new_sensor(config[CONF_TEMPERATURE_4])
            cg.add(var.set_temperature4_sensor(sens))
        if CONF_PUMP_SPEED_1 in config:
            sens = await sensor.new_sensor(config[CONF_PUMP_SPEED_1])
            cg.add(var.set_pump_speed1_sensor(sens))
        if CONF_PUMP_SPEED_2 in config:
            sens = await sensor.new_sensor(config[CONF_PUMP_SPEED_2])
            cg.add(var.set_pump_speed2_sensor(sens))
        if CONF_OPERATING_HOURS_1 in config:
            sens = await sensor.new_sensor(config[CONF_OPERATING_HOURS_1])
            cg.add(var.set_operating_hours1_sensor(sens))
        if CONF_OPERATING_HOURS_2 in config:
            sens = await sensor.new_sensor(config[CONF_OPERATING_HOURS_2])
            cg.add(var.set_operating_hours2_sensor(sens))
        if CONF_HEAT_QUANTITY in config:
            sens = await sensor.new_sensor(config[CONF_HEAT_QUANTITY])
            cg.add(var.set_heat_quantity_sensor(sens))
        if CONF_TIME in config:
            sens = await sensor.new_sensor(config[CONF_TIME])
            cg.add(var.set_time_sensor(sens))
        if CONF_VERSION in config:
            sens = await sensor.new_sensor(config[CONF_VERSION])
            cg.add(var.set_version_sensor(sens))

    elif config[CONF_MODEL] == CONF_CUSTOM:
        if CONF_COMMAND in config:
          cg.add(var.set_command(config[CONF_COMMAND]))
        if CONF_SOURCE in config:
          cg.add(var.set_source(config[CONF_SOURCE]))
        if CONF_DEST in config:
          cg.add(var.set_dest(config[CONF_DEST]))
        if CONF_LAMBDA in config:
          lambda_ = await cg.process_lambda(
              config[CONF_LAMBDA], [(cg.std_vector.template(cg.uint8), "x")], return_type=cg.void
          )
          cg.add(var.set_message_handler(lambda_))


    vbus = await cg.get_variable(config[CONF_VBUS_ID])
    cg.add(vbus.register_listener(var))
