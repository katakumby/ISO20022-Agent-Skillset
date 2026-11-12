---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["21 sese.027.001.09 SecuritiesTransactionCancellationRequestStatusAdviceV09", "21.4 Message Building Blocks", "21.4.3 ProcessingStatus <PrcgSts>", "21.4.3.6 Denied <Dnd>"]
file_pages: [716, 717]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.027.001.09"]
---

# 21.4.3.6 Denied <Dnd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 716 to 717.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 716

```text
Proprietary <Prtry> contains the following elements (see "ProprietaryStatusAndReason6" on
page 1877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProprietaryStatus <PrtrySts> [1..1] ± 1878
   ProprietaryReason <PrtryRsn> [0..*] ± C1 1878
21.4.3.6  Denied <Dnd>
Presence: [1..1]
Definition: Instruction/Request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus15Choice" on page 1939 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1940
Or}   Reason <Rsn> [1..*]  1940
     Code <Cd> [1..1] ± 1940
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1940
21.4.3.7  Cancelled <Canc>
Presence: [1..1]
Definition: Cancellation requested executed.
Cancelled <Canc> contains one of the following elements (see "CancellationStatus15Choice" on
page 1921 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1921
Or}   Reason <Rsn> [1..*]  1922
     Code <Cd> [1..1] ± 1922
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1922
21.4.4 TransactionDetails <TxDtls>
Presence: [0..1]
Definition: Identifies the details of the transaction.
Impacted by: C19 "SafekeepingAccountOrBlockChainAddress1Rule", C21
"SafekeepingAccountOrBlockChainAddress2Rule", C23
"SafekeepingAccountOrBlockChainAddress3Rule"
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 716 March 2026
```

## File page 717

```text
TransactionDetails <TxDtls> contains the following TransactionDetails178 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 718
   SafekeepingAccount <SfkpgAcct> [0..1] ± 718
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 718
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
719
   SettlementQuantity <SttlmQty> [1..1] ± 720
   SettlementAmount <SttlmAmt> [0..1] ± 720
   DigitalPaymentSettlement <DgtlPmtSttlm> [0..1]  720
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C8, C9,
C11,
C12,
C14
721
     ElectronicMoneyTokenSettlementQuantity
<ElctrncMnyTknSttlmQty>
[1..1] Quantity 722
     CashSettlementSystemPlace <CshSttlmSysPlc> [0..1]  722
{Or       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 722
Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C4 722
Or}       LEI <LEI> [1..1] IdentifierSet 723
   TradeDate <TradDt> [0..1] ± 723
   SettlementDate <SttlmDt> [1..1] ± 723
   DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C15,
C16,
C17,
C18
723
   ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C15,
C16,
C17,
C18
724
   Investor <Invstr> [0..1] ± 725
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Approved by the Securities SEG on 27 January 2026 sese.027.001.09
SecuritiesTransactionCancellationRequestStatusAd
viceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 717 March 2026
```

