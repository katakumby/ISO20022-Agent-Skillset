---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.17 CallableIndicator <CllblInd>"]
file_pages: [205]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.17 CallableIndicator <CllblInd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 205 to 205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 205

```text
Definition: Specifies whether the payment of the coupon (interest) on a bond is off the normal schedule.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.17  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.18  CPProgram <CPPrgm>
Presence: [0..1]
Definition: The program under which a commercial paper is issued. The values that are most used are:
0 = N/A
1 = 3(a)3
2 = 4(2)
3 = 3(a)4
4 = 3(c)7
5 = 144A
6 = 3(a)2
99 = Other.
Datatype: "Number" on page 532
13.1.2.3.19  CPRegistrationType <CPRegnTp>
Presence: [0..1]
Definition: Registration type of a commercial paper issuance.
Datatype: "Max350Text" on page 534
13.1.2.3.20  InterestAccrualDate <IntrstAcrlDt>
Presence: [0..1]
Definition: Start date used for calculating accrued interest on debt instruments which are being sold
between interest payment dates. Often but not always the same as the issue date and the dated date.
Datatype: "ISODateTime" on page 529
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 205 March 2024
```

