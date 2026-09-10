from client import BiquadIIRFilter

def main():
    print("=== Testing Biquad IIR Lowpass Filter ===")
    biquad = BiquadIIRFilter(cutoff_ratio=0.2)

    samples = [1.0] * 10
    filtered = [biquad.process_sample(s) for s in samples]

    print("Step response over 10 samples:")
    for idx, val in enumerate(filtered):
        print(f"  n={idx}: {round(val, 4)}")

    assert filtered[-1] > 0.8
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
