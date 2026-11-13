---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.2 Structure"]
file_pages: [785, 786]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 785 to 786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 785

```text
32.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ReqForTrfStsRpt> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 0
   RequestDetails <ReqDtls> [1..*]  C7, C8 0
     Reference <Ref> [0..1]  791
{Or       PreviousReference <PrvsRef> [1..1] ± 791
Or}       OtherReference <OthrRef> [1..1] ± 791
     TypeOfRequest <TpOfReq> [0..1]  791
{Or       Code <Cd> [1..1] CodeSet 792
Or}       Proprietary <Prtry> [1..1] ± 792
     MasterReference <MstrRef> [0..1] Text 792
     TransferReference <TrfRef> [1..1] ± 792
     ClientReference <ClntRef> [0..1] ± 793
     CancellationReference <CxlRef> [0..1] Text 793
     Instrument <Instrm> [0..1]  793
{Or       Security <Scty> [1..1]  C6 794
         Identification <Id> [1..1]  795
{Or           ISIN <ISIN> [1..1] IdentifierSet 796
Or           SEDOL <SEDOL> [1..1] IdentifierSet 796
Or           CUSIP <CUSIP> [1..1] IdentifierSet 797
Or           RIC <RIC> [1..1] IdentifierSet 797
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 797
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 797
Or           CTA <CTA> [1..1] IdentifierSet 797
Or           QUICK <QUICK> [1..1] IdentifierSet 797
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 797
Or           Dutch <Dtch> [1..1] IdentifierSet 798
Or           Valoren <Vlrn> [1..1] IdentifierSet 798
Or           Sicovam <SCVM> [1..1] IdentifierSet 798
Or           Belgian <Belgn> [1..1] IdentifierSet 798
Or           Common <Cmon> [1..1] IdentifierSet 798
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 785 May 2026
```

## File page 786

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           DTI <DTI> [1..1] IdentifierSet 798
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  798
             Identification <Id> [1..1] Text 799
             IdentificationSource <IdSrc> [1..1] ± 799
         Name <Nm> [0..1] Text 799
         ShortName <ShrtNm> [0..1] Text 799
         ClassificationType <ClssfctnTp> [0..1] ± 799
Or       CashAsset <CshAsst> [1..1] ± C5 799
Or}       OtherAsset <OthrAsst> [1..1] ± 800
     InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  800
       OwnerIdentification <OwnrId> [0..1] ± 801
       AccountIdentification <AcctId> [0..1] Text 801
       AccountDesignation <AcctDsgnt> [0..1] Text 801
       AccountName <AcctNm> [0..1] Text 802
       Type <Tp> [0..1] ± 802
       Servicer <Svcr> [0..1] ± 802
       SubAccountDetails <SubAcctDtls> [0..1] ± 802
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 803
     IntermediaryInformation <IntrmyInf> [0..*] ± 803
     QueryInformation <QryInf> [0..*]  803
       QueryType <QryTp> [0..1] ± 804
       Query <Qry> [1..1] Text 804
       QueryReason <QryRsn> [0..1] Text 804
       RejectionReason <RjctnRsn> [0..1]  804
{Or         Code <Cd> [1..1] CodeSet 805
Or}         Proprietary <Prtry> [1..1] ± 807
     RequestIssuer <ReqIssr> [0..1] ± 807
     RequestRecipient <ReqRcpt> [0..1] ± 807
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 0
   Extension <Xtnsn> [0..*] ± C4 0
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 786 May 2026
```

