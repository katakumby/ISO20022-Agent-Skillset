---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.3 Debt <Debt>", "27.4.2.2.3.17 CallableIndicator <CllblInd>"]
file_pages: [680]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.3.17 CallableIndicator <CllblInd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 680 to 680.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 680

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.17  CallableIndicator <CllblInd>
Presence: [0..1]
Definition: Indicates whether the issuer has the right to pay the security prior to maturity. Also called
RetractableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.18  CPProgram <CPPrgm>
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
Datatype: "Number" on page 3324
27.4.2.2.3.19  CPRegistrationType <CPRegnTp>
Presence: [0..1]
Definition: Registration type of a commercial paper issuance.
Datatype: "Max350Text" on page 3328
27.4.2.2.3.20  InterestAccrualDate <IntrstAcrlDt>
Presence: [0..1]
Definition: Start date used for calculating accrued interest on debt instruments which are being sold
between interest payment dates. Often but not always the same as the issue date and the dated date.
Datatype: "ISODateTime" on page 3320
27.4.2.2.3.21  PutableIndicator <PutblInd>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 680 August 2026
```

