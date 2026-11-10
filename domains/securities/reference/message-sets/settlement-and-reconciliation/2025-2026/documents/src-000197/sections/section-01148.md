---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.57 BlockChainAddressWallet1", "35.1.16.57.3 Name <Nm>"]
file_pages: [1595]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.57.3 Name <Nm>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1595 to 1595.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1595

```text
Definition: Specifies the type of securities account.
Type <Tp> contains one of the following elements (see "PurposeCode7Choice" on page 1603 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1603
Or}   Proprietary <Prtry> [1..1] ± 1604
35.1.16.57.3  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max70Text" on page 2192
35.1.16.57.4  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 2192
35.1.16.58  AdditionalParameters33
Definition: Specifies additional parameters to the message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 1595
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 1596
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 1596
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 1596
   PoolIdentification <PoolId> [0..1] Text 1596
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1596
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 1596
   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[0..1] Text 1597
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 1597
35.1.16.58.1  PartialSettlement <PrtlSttlm>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1595 March 2026
```

