---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.2 Structure"]
file_pages: [667, 668]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 667 to 668.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 667

```text
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnMvmntRvslAdvc> [1..1]  C2, C12,
C17,
C15
   MovementConfirmationIdentification <MvmntConfId> [1..1] ± 671
   OtherDocumentIdentification <OthrDocId> [0..*] ± 671
   EventsLinkage <EvtsLkg> [0..*] ± 672
   ReversalReason <RvslRsn> [0..1]  C3 672
     Reason <Rsn> [1..1]  673
{Or       Code <Cd> [1..1] CodeSet 673
Or}       Proprietary <Prtry> [1..1] ± 673
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 674
   TransactionIdentification <TxId> [0..1]  674
     MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 674
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C16 674
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 675
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 675
     ClassActionNumber <ClssActnNb> [0..1] Text 675
     EventType <EvtTp> [1..1] ± C10 675
     FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C13,
C14,
C18
676
     FractionalQuantity <FrctnlQty> [0..1] ± C9 677
   AccountDetails <AcctDtls> [1..1]  C19,
C20,
C21
677
     SafekeepingAccount <SfkpgAcct> [0..1] Text 678
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 678
     ConfirmedBalance <ConfdBal> [1..1] ± 678
   CorporateActionDetails <CorpActnDtls> [0..1]  679
     DateDetails <DtDtls> [0..1]  679
       RecordDate <RcrdDt> [0..1] ± 679
       ExDividendDate <ExDvddDt> [0..1] ± 680
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 667 February 2026
```

## File page 668

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     EventStage <EvtStag> [0..1] ± 680
     AdditionalBusinessProcessIndicator <AddtlBizPrcInd> [0..1] ± 680
     FollowingEventTypeIndicator <FllwngEvtTpInd> [0..1] ± 681
     LotteryType <LtryTp> [0..1] ± 681
   CorporateActionConfirmationDetails <CorpActnConfDtls> [1..1]  681
     OptionNumber <OptnNb> [1..1] ± 682
     OptionType <OptnTp> [1..1] ± 682
     SecuritiesMovementDetails <SctiesMvmntDtls> [0..*]  683
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C7, C8,
C13,
C14,
C18
683
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 684
       PostingQuantity <PstngQty> [1..1] ± 684
       PostingDate <PstngDt> [1..1] ± 685
       OriginalPostingDate <OrgnlPstngDt> [0..1] ± 685
     CashMovementDetails <CshMvmntDtls> [0..*]  685
       CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 686
       Account <Acct> [0..1]  686
{Or         CashAccount <CshAcct> [1..1] ± 686
Or         ChargesAccount <ChrgsAcct> [1..1] ± 687
Or}         TaxAccount <TaxAcct> [1..1] ± 687
       PostingDate <PstngDt> [1..1] ± 687
       OriginalPostingDate <OrgnlPstngDt> [0..1] ± 687
       ValueDate <ValDt> [0..1] Date 688
       PostingAmount <PstngAmt> [1..1] Amount C1, C6 688
   AdditionalInformation <AddtlInf> [0..1]  688
     AdditionalText <AddtlTxt> [0..*] Text 689
     NarrativeVersion <NrrtvVrsn> [0..*] Text 689
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 689
     TaxationConditions <TaxtnConds> [0..*] Text 689
   IssuerAgent <IssrAgt> [0..*] ± 689
   PayingAgent <PngAgt> [0..*] ± 690
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 668 February 2026
```

