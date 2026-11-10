---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.16 AdditionalPhysicalOrRegistrationDetails <AddtlPhysOrRegnDtls>", "26.4.18.1 ProcessingStatus <PrcgSts>", "26.4.18.1.6 CancellationRequested <CxlReqd>"]
file_pages: [875]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.18.1.6 CancellationRequested <CxlReqd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 875 to 875.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 875

```text
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
26.4.18.1.6  CancellationRequested <CxlReqd>
Presence: [1..1]
Definition: Cancellation request from your counterparty for this transaction is pending waiting for your
cancellation request.
Impacted by: C7 "AdditionalReasonInforrmationRule"
CancellationRequested <CxlReqd> contains the following elements (see "ProprietaryReason4" on
page 1899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
26.4.18.2  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [0..1]
Definition: Provides the matching status of an instruction as known by the account servicer based on an
allegement. At this time no matching took place on the market (at the CSD/ICSD).
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 875 March 2026
```

