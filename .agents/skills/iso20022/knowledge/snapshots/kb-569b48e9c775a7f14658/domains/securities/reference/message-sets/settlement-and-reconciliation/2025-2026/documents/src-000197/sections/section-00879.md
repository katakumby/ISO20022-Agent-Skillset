---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.6 ModificationProcessingStatus <ModPrcgSts>", "33.4.6.6 Modified <Modfd>", "33.4.6.6.2 Reason <Rsn>", "33.4.6.6.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [1312]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.6.6.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1312 to 1312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1312

```text
33.4.6.6.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
33.4.6.7  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary status.
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
33.4.7 TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1312 March 2026
```

