---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.1 BillingReport <BllgRpt>", "3.4.2.1.1 RegulatoryData <RgltryData>", "3.4.2.1.1.4 PaymentMethod <PmtMtd>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.1.1.4 PaymentMethod <PmtMtd>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
3.4.2.1.1.4  PaymentMethod <PmtMtd>
Presence: [0..1]
Definition: Method of payment for the remittance of the CSD or NCB to the invoicing party.
PaymentMethod <PmtMtd> contains one of the following PaymentMethod3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 40
Or}   Proprietary <Prtry> [1..1] Text 40
3.4.2.1.1.4.1  Code <Cd>
Presence: [1..1]
Definition: Method of payment for the remittance of the CSD or NCB to the invoicing party, in a coded
form.
Datatype: "ExternalPaymentMethode1Code" on page 146
3.4.2.1.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Method of payment for the remittance of the CSD or the NCB to the invoicing party, in a
proprietary free text format.
Datatype: "Max210Text" on page 152
3.4.2.1.2  Service <Svc>
Presence: [0..1]
Definition: Identification of the service or system for which the billing information is provided.
Service <Svc> contains the following SystemAndCurrency1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemIdentification <SysId> [1..1] ± 40
   SystemCurrency <SysCcy> [0..1] CodeSet C1 41
3.4.2.1.2.1  SystemIdentification <SysId>
Presence: [1..1]
Definition: Unique and unambiguous identification of the system, as assigned by the system
administrator.
SystemIdentification <SysId> contains one of the following elements (see
"SystemIdentification2Choice" on page 142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   MarketInfrastructureIdentification <MktInfrstrctrId> [1..1] ± 142
Or}   Country <Ctry> [1..1] CodeSet C3 142
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 40 December 2025
```

