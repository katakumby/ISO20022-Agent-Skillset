---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.87 PendingProcessingReason22Choice", "35.1.29.87.2 Proprietary <Prtry>"]
file_pages: [2014]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.87.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2014 to 2014.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2014

```text
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
OTHR Other Other. See Narrative.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
CERT WrongCertificatesNumbers Certificate number error.
35.1.29.87.2  Proprietary <Prtry>
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
35.1.29.88  PendingProcessingStatus23Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2015
Or}   Reason <Rsn> [1..*]  2015
     Code <Cd> [1..1] ± 2015
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2015
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2014 March 2026
```

