from device_model import DeviceModel

if __name__ == "__main__":
    #  1 READ ALL DEVICE MODELS
    print("ALL DEVICE MODELS:")
    device_models = DeviceModel.read_all()
    for device in device_models:
        print(device)

    # 2 GET MODEL BY ID
    print("DEVICE MODEL BY ID(1):")
    try:
        print(DeviceModel.get_by_id(1))
    except Exception as e:
        print(e.__str__())

    # 3 CREATE DEVICE MODEL
    print("CREATING DEVICE MODEL:")
    try:
        new_device_object = DeviceModel.create("Bosch", "TIS 30129RW", 1.4, 3, 1, 0.5, 1000, 1500)
        print(new_device_object)
    except Exception as e:
        print(e)

    # 4 DELETE DEVICE MODEL
    print("DELETING DEVICE MODEL BY ID(8):")
    try:
        if DeviceModel.delete(8):
            print("Device model deleted!")
    except Exception as e:
        print(e)

    # 5 UPDATE DEVICE MODEL
    print("UPDATING DEVICE MODEL:")
    try:
        model_to_update = DeviceModel.get_by_id(3)
        model_to_update = model_to_update.update({"model_number": "1234567", "milk_capacity_kgs": "1.7"})
        print(model_to_update)
        print(f"Updated values: number - {model_to_update.model_number}, milk - {model_to_update.milk_capacity_kgs}kg")
    except Exception as e:
        print(e)

