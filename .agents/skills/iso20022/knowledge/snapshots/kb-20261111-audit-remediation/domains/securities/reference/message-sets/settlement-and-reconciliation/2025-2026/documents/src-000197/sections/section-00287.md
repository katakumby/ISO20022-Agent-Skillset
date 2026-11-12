---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.4 Message Building Blocks", "12.4.6 AdditionalQueryParameters <AddtlQryParams>", "12.4.6.2 Reason <Rsn>", "12.4.6.2.9 PendingProcessingReason <PdgPrcgRsn>", "12.4.6.2.9.2 Proprietary <Prtry>"]
file_pages: [429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.4.6.2.9.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 429 to 429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 429

```text
CodeName Name Definition
OTHR Other Other. See Narrative.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
CERT WrongCertificatesNumbers Certificate number error.
12.4.6.2.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
12.4.6.2.10  RejectionReason <RjctnRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction/request has a rejected status.
RejectionReason <RjctnRsn> contains one of the following elements (see
"RejectionReason45Choice" on page 1941 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1941
Or}   Proprietary <Prtry> [1..1] ± 1944
12.4.6.2.11  RepairReason <RprRsn>
Presence: [0..1]
Definition: Specifies the reason why the instruction is in repair.
RepairReason <RprRsn> contains one of the following elements (see "RepairReason11Choice" on
page 1989 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1989
Or}   Proprietary <Prtry> [1..1] ± 1991
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 429 March 2026
```

