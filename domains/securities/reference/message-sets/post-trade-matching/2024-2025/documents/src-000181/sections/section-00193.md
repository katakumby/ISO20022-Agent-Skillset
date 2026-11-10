---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.4 AmountOrRate2Choice", "7.1.3.4.2 Rate <Rate>"]
file_pages: [246]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.4.2 Rate <Rate>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 246 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
Note: The decimal separator is a dot.
7.1.3.4.2  Rate <Rate>
Presence: [1..1]
Definition: Amount expressed as a rate.
Datatype: "PercentageRate" on page 667
7.1.4 Basic Securities Registration
7.1.4.1  RegistrationParameters3
Definition: Information related to registration of securities.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CertificationIdentification <CertfctnId> [0..1] Text 246
   CertificationDateTime <CertfctnDtTm> [0..1] ± 246
   RegistrarAccount <RegarAcct> [0..1] Text 246
   CertificateNumber <CertNb> [0..*] ± C21 246
7.1.4.1.1  CertificationIdentification <CertfctnId>
Presence: [0..1]
Definition: Identification assigned to a deposit.
Datatype: "Max35Text" on page 669
7.1.4.1.2  CertificationDateTime <CertfctnDtTm>
Presence: [0..1]
Definition: Date/time at which the certificates in the deposit were validated by the agent.
CertificationDateTime <CertfctnDtTm> contains one of the following elements (see
"DateAndDateTime1Choice" on page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.4.1.3  RegistrarAccount <RegarAcct>
Presence: [0..1]
Definition: Account at the registrar where financial instruments are registered.
Datatype: "Max35Text" on page 669
7.1.4.1.4  CertificateNumber <CertNb>
Presence: [0..*]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 246 February 2025
```

