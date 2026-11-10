---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.4 Message Building Blocks", "13.4.6 AccountOwner <AcctOwnr>", "13.4.7.8 ModificationProcessingStatus <ModPrcgSts>", "13.4.7.8.6 Modified <Modfd>", "13.4.7.8.6.2 Reason <Rsn>", "13.4.7.8.6.2.1 Code <Cd>"]
file_pages: [453]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.4.7.8.6.2.1 Code <Cd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 453 to 453.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 453

```text
Reason <Rsn> contains the following ModificationReason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  453
{Or     Code <Cd> [1..1] CodeSet 453
Or}     Proprietary <Prtry> [1..1] ± 453
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 454
13.4.7.8.6.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the transaction is modified.
Code <Cd> contains one of the following ModificationReason4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 453
Or}   Proprietary <Prtry> [1..1] ± 453
13.4.7.8.6.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is modified, or the related modification
request is executed.
Datatype: "ModifiedStatusReason1Code" on page 2087
CodeName Name Definition
MDBY ModifiedByYourself Modification of a transaction by the
account owner.
OTHR Other Other. See Narrative.
13.4.7.8.6.2.1.2  Proprietary <Prtry>
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
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 453 March 2026
```

