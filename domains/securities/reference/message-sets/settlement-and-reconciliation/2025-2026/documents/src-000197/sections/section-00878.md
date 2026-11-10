---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.6 ModificationProcessingStatus <ModPrcgSts>", "33.4.6.6 Modified <Modfd>", "33.4.6.6.2 Reason <Rsn>", "33.4.6.6.2.1 Code <Cd>"]
file_pages: [1311]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.6.6.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1311 to 1311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1311

```text
Reason <Rsn> contains the following ModificationReason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  1311
{Or     Code <Cd> [1..1] CodeSet 1311
Or}     Proprietary <Prtry> [1..1] ± 1311
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1312
33.4.6.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the transaction is modified.
Code <Cd> contains one of the following ModificationReason4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1311
Or}   Proprietary <Prtry> [1..1] ± 1311
33.4.6.6.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is modified, or the related modification
request is executed.
Datatype: "ModifiedStatusReason1Code" on page 2087
CodeName Name Definition
MDBY ModifiedByYourself Modification of a transaction by the
account owner.
OTHR Other Other. See Narrative.
33.4.6.6.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is modified, or the related modification
request is executed.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1311 March 2026
```

