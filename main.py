import math

angles = [0,90,45,50,60,30,15,-90,-45,-27]

dbm_measurements = [-56,-66,-58,-59,-59.50,-57,-56,-76,-57,-56]

noise_floor_dbm = -92

bandwidth_khz = 50

def calculate_bandwidth_hz(bandwidth_khz):
    return bandwidth_khz * 1000

def calculate_snr_dbs(dbm_measurements: list, noise_floor_dbm) -> list:
    snr_db_measurements = []
    for dbm in dbm_measurements:
        snr_value = dbm - noise_floor_dbm
        snr_db_measurements.append(snr_value)
    return snr_db_measurements

def calculate_snr_power_ratios(snr_measurements: list) -> list:
    snr_power_ratios = []
    for snr_db in snr_measurements:
        power_ratio = 10 ** (snr_db/10)
        snr_power_ratios.append(power_ratio)

    return snr_power_ratios

def calculate_max_bit_rate(bandwidth_hz, snr_power_ratios: list) -> list:
    max_data_speeds = []
    for snr_ratio in snr_power_ratios:
        data_speed = bandwidth_hz * math.log2(1 + snr_ratio)
        max_data_speeds.append(data_speed)

    return max_data_speeds



def main():
    bandwidth = calculate_bandwidth_hz(bandwidth_khz)

    snr_dbs = calculate_snr_dbs(dbm_measurements, noise_floor_dbm)

    snr_power_ratios = calculate_snr_power_ratios(snr_dbs)

    max_bit_rates = calculate_max_bit_rate(bandwidth, snr_power_ratios)

    print(f"BANDWIDTH USED: {bandwidth_khz} kHz ({bandwidth} Hz)")
    print(f"NOISE FLOOR: {noise_floor_dbm} dBm")
    print("-----------------------------------------------")


    for angle, dbm, snr_db, snr_ratio, bit_rate in zip(
        angles,
        dbm_measurements,
        snr_dbs,
        snr_power_ratios,
        max_bit_rates
    ):
        print(f"Angle: {angle} degrees")
        print(f"dBm Measurement: {dbm} dBm")
        print(f"Signal to Noise Values (in dB): {snr_db}")
        print(f"Signal to Noise Power Ratios: {snr_ratio}")
        print(f"Channel Capacity (Bits Per Second): {bit_rate}")
        print("-----------------------------------------------")


if __name__ == "__main__":
    main()
