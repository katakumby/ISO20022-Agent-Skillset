---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>", "22.4.9.13 TerminationTransactionAmount <TermntnTxAmt>"]
file_pages: [752, 753, 754]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.9.13 TerminationTransactionAmount <TermntnTxAmt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 752 to 754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 752

```text
Definition: Interest amount that has accrued in between coupon payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
22.4.9.13  TerminationTransactionAmount <TermntnTxAmt>
Presence: [0..1]
Definition: Total amount of money to be settled to terminate the transaction.
TerminationTransactionAmount <TermntnTxAmt> contains the following elements (see
"AmountAndDirection21" on page 1377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1377
22.4.9.14  SecondLegNarrative <ScndLegNrrtv>
Presence: [0..1]
Definition: Provides additional information about the second leg in narrative form.
Datatype: "Max140Text" on page 2191
22.4.10 SettlementParameters <SttlmParams>
Presence: [1..1]
Definition: Parameters which explicitly state the conditions that must be fulfilled before a particular
transaction of a financial instrument can be settled. These parameters are defined by the instructing
party in compliance with settlement rules in the market the transaction will settle in.
Impacted by: C9 "CashClearingSystemRule", C44 "SettlementDetailsRule"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 752 March 2026
```

## File page 753

```text
SettlementParameters <SttlmParams> contains the following elements (see "SettlementDetails224"
on page 1832 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldIndicator <HldInd> [0..1] Indicator 1832
   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 1832
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1833
   PartialSettlementIndicator <PrtlSttlmInd> [0..1] CodeSet 1833
   BeneficialOwnership <BnfclOwnrsh> [0..1] ± 1833
   CashClearingSystem <CshClrSys> [0..1] ± 1834
   MarketClientSide <MktClntSd> [0..1] ± 1834
   Registration <Regn> [0..1] ± 1834
   RepurchaseType <RpTp> [0..1] ± 1834
   SecuritiesRTGS <SctiesRTGS> [0..1] ± 1835
   StampDutyTaxBasis <StmpDtyTaxBsis> [0..1] ± 1835
Constraints
• CashClearingSystemRule
The CashClearingSystem codes are to be used only by agents directly involved in the settlement
process, such as local settlement agents, CSDs and central banks.
• SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed between
account owner and account servicer.
22.4.11 DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Impacted by: C8 "BookTransferGuideline", C15 "DepositoryGuideline", C27 "Party2PresenceRule", C28
"Party3PresenceRule", C29 "Party4PresenceRule", C30 "Party5PresenceRule", C43
"SettlementChainGuideline"
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 753 March 2026
```

## File page 754

```text
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties126" on page 1767 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1769
   Party1 <Pty1> [0..1] ± C29,
C31
1770
   Party2 <Pty2> [0..1] ± C29,
C31
1771
   Party3 <Pty3> [0..1] ± C29,
C31
1771
   Party4 <Pty4> [0..1] ± C29,
C31
1772
   Party5 <Pty5> [0..1] ± C29,
C31
1773
Constraints
• BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC is to be used.
Country code should be used for settlement taking place outside of an institution published in the
PSET's BIC list. This includes physical deliveries and investment funds not settling at a CSD.
The format and content of the settlement party sequences will comply with the market practices
published for the counterparty depository included in the message.
For more details, see the relevant market practice document on www.smpg.info.
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 754 March 2026
```

