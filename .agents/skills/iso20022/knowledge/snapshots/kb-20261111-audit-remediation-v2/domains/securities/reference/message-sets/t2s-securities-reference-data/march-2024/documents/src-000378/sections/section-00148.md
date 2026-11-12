---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.35 CurrentFactor <CurFctr>"]
file_pages: [210]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.35 CurrentFactor <CurFctr>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 210 to 210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 210

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.2.3.35  CurrentFactor <CurFctr>
Presence: [0..1]
Definition: Identifies the current factor expressed as a decimal between 0 and 1 defining the outstanding
principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 532
13.1.2.3.36  NextFactor <NxtFctr>
Presence: [0..1]
Definition: Identifies the new factor expressed as a decimal between 0 and 1 defining the outstanding
principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 532
13.1.2.3.37  PreviousFactor <PrvsFctr>
Presence: [0..1]
Definition: Identifies the previous factor expressed as a decimal between 0 and 1 defining the
outstanding principal of the bond (for factored securities).
Datatype: "PercentageRate" on page 532
13.1.2.3.38  Pieces <Pcs>
Presence: [0..1]
Definition: Number of pieces composing a pool of financial assets.
Datatype: "DecimalNumber" on page 532
13.1.2.3.39  PoolsMaximum <PlsMax>
Presence: [0..1]
Definition: Collection of assets by which a security is backed.
Datatype: "DecimalNumber" on page 532
13.1.2.3.40  PoolsPerMillion <PlsPerMln>
Presence: [0..1]
Definition: Indicates per million the collection of loans, mortgages or other assets assembled by an
originator as the basis for a security.
Datatype: "DecimalNumber" on page 532
13.1.2.3.41  PoolsPerLot <PlsPerLot>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 210 March 2024
```

