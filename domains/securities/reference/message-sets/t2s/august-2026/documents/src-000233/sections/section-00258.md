---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["15 camt.077.001.01 BillingReportV01", "15.4 Message Building Blocks", "15.4.2 BillingReportOrError <BllgRptOrErr>", "15.4.2.2 CancellationReport <CxlRpt>", "15.4.2.2.1 RegulatoryData <RgltryData>", "15.4.2.2.1.4 PaymentMethod <PmtMtd>"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 15.4.2.2.1.4 PaymentMethod <PmtMtd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
15.4.2.2.1.4  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Method of payment for the remittance of the CSD or NCB to the invoicing party.
PaymentMethod <PmtMtd> contains one of the following PaymentMethod3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 337
Or}   Proprietary <Prtry> [1..1] Text 337
15.4.2.2.1.4.1  Code <Cd>
Presence: [1..1]
Definition: Method of payment for the remittance of the CSD or NCB to the invoicing party, in a coded
form.
Datatype: "ExternalPaymentMethode1Code" on page 3243
15.4.2.2.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Method of payment for the remittance of the CSD or the NCB to the invoicing party, in a
proprietary free text format.
Datatype: "Max210Text" on page 3327
15.4.2.2.2  Service <Svc>
Presence: [0..1]
Definition: Identification of the service or system for which the billing cancellation is provided.
Service <Svc> contains the following SystemAndCurrency1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [1..1] ± 337
   SystemCurrency <SysCcy> [0..1] CodeSet C1 338
15.4.2.2.2.1  SystemIdentification <SysId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the system, as assigned by the system
administrator.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 3203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 3203
Or}   Country <Ctry> [1..1] CodeSet C3 3203
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.077.001.01 BillingReportV01
Target2-Securities 337 August 2026
```

