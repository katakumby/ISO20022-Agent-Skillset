---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["3 camt.077.001.01 BillingReportV01", "3.4 Message Building Blocks", "3.4.2 BillingReportOrError <BllgRptOrErr>", "3.4.2.2 CancellationReport <CxlRpt>", "3.4.2.2.6 CancellationReason <CxlRsn>", "3.4.2.2.6.1 Code <Cd>"]
file_pages: [110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.077.001.01"]
---

# 3.4.2.2.6.1 Code <Cd>

Source: [src-000346](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 110 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 110

```text
CancellationReason <CxlRsn> contains one of the following CancellationReason16Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 110
Or}   Proprietary <Prtry> [1..1] Text 110
3.4.2.2.6.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the cancellation request, in a coded form.
Datatype: "Max4AlphaNumericText" on page 153
3.4.2.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the cancellation request, in a proprietary form.
Datatype: "Max35Text" on page 153
3.4.2.3  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates that an operational error has been issued during the processing of the related
request.
OperationalError <OprlErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  110
{Or     Code <Cd> [1..1] CodeSet 110
Or}     Proprietary <Prtry> [1..1] Text 111
   Description <Desc> [0..1] Text 111
3.4.2.3.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 110
Or}   Proprietary <Prtry> [1..1] Text 111
3.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.077.001.01 BillingReportV01
Target2-Securities - Billing 110 December 2025
```

