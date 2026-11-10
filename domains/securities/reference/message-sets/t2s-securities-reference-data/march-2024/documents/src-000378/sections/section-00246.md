---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.1 SecurityStatus <SctySts>", "13.1.6.3.1.1 Code <Cd>"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.1.1 Code <Cd>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 331
Or}   Proprietary <Prtry> [1..1] ± 331
13.1.6.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Datatype: "SecurityStatus2Code" on page 523
CodeName Name Definition
ACTV Active The status is active.
INAC Inactive The status is inactive.
SUSP Suspended The status is suspended.
13.1.6.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Security status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.3.2  FinancialInstrumentName <FinInstrmNm>
Presence: [0..*]
Definition: Name of the security.
FinancialInstrumentName <FinInstrmNm> contains the following FinancialInstrumentName2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISOShortName <ISOShrtNm> [0..1] Text 332
   ISOLongName <ISOLngNm> [0..1] Text 332
   ValidFrom <VldFr> [0..1] ± 332
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 331 March 2024
```

