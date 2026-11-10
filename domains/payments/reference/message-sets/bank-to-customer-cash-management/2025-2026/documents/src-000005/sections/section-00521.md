---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.24 UnderlyingAllocation <UndrlygAllcn>", "4.4.2.14.18.2.24.5 Reference <Ref>"]
file_pages: [750]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.24.5 Reference <Ref>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 750 to 750.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 750

```text
4.4.2.14.18.2.24.5  Reference <Ref>
Presence: [1..1]
Definition: Reference for the allocation.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.24.6  RelatedReferences <RltdRefs>
Presence: [0..*]
Definition: Reference relating to the allocation which is meaningful to both parties (for example the
original Securities Settlement Transaction Identification).
RelatedReferences <RltdRefs> contains one of the following elements (see "References80Choice" on
page 836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesSettlementTransactionIdentification
<SctiesSttlmTxId>
[1..1] Text 837
Or   IntraPositionMovementIdentification <IntraPosMvmntId> [1..1] Text 837
Or   IntraBalanceMovementIdentification <IntraBalMvmntId> [1..1] Text 837
Or   AccountServicerTransactionIdentification <AcctSvcrTxId> [1..1] Text 837
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 838
Or   CounterpartyMarketInfrastructureTransactionIdentificatio
n <CtrPtyMktInfrstrctrTxId>
[1..1] Text 838
Or   PoolIdentification <PoolId> [1..1] Text 838
Or   CommonIdentification <CmonId> [1..1] Text 838
Or   TradeIdentification <TradId> [1..1] Text 838
Or   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 838
Or}   OtherTransactionIdentification <OthrTxId> [1..1] Text 838
4.4.2.14.18.2.25  CashDeposit <CshDpst>
Presence: [0..*]
Definition: Provides the details of a cash deposit for an amount of money in cash notes and/or coins.
CashDeposit <CshDpst> contains the following elements (see "CashDeposit1" on page 823 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoteDenomination <NoteDnmtn> [1..1] Amount C1, C7 823
   NumberOfNotes <NbOfNotes> [1..1] Text 824
   Amount <Amt> [1..1] Amount C1, C7 824
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
750 March 2026
```

