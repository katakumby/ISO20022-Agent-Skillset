---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.74 Linkages40"]
file_pages: [1619]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.74 Linkages40

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1619 to 1619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1619

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.74  Linkages40
Definition: Information related to a linked transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] ± 1619
35.1.16.74.1  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Reference <Ref> contains one of the following elements (see "References47Choice" on page 1488 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 1488
Or   PoolIdentification <PoolId> [1..1] Text 1488
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 1488
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 1488
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 1488
35.1.16.75  NumberCount1Choice
Definition: Choice of number count type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 1620
Or}   TotalNumber <TtlNb> [1..1]  C9, C6 1620
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 1620
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 1620
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1619 March 2026
```

