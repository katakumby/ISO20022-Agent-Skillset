---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.17 CardTransaction <CardTx>"]
file_pages: [340, 341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.17 CardTransaction <CardTx>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 340 to 341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 340

```text
Interest <Intrst> contains the following elements (see "TransactionInterest4" on page 852 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalInterestAndTaxAmount <TtlIntrstAndTaxAmt> [0..1] Amount C1, C5 852
   Record <Rcrd> [0..*]  853
     Amount <Amt> [1..1] Amount C1, C5 853
     CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 854
     Type <Tp> [0..1]  854
{Or       Code <Cd> [1..1] CodeSet 854
Or}       Proprietary <Prtry> [1..1] Text 854
     Rate <Rate> [0..1]  854
       Type <Tp> [1..1] ± 855
       ValidityRange <VldtyRg> [0..1] ± 855
     FromToDate <FrToDt> [0..1] ± 855
     Reason <Rsn> [0..1] Text 855
     Tax <Tax> [0..1]  856
       Identification <Id> [0..1] Text 856
       Rate <Rate> [0..1] Rate 856
       Amount <Amt> [0..1] Amount C1, C5 856
3.4.2.15.17  CardTransaction <CardTx>
Presence: [0..1]
Definition: Provides details of the card transaction included in the entry amount, when globalised by the
account servicer.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
340 March 2026
```

## File page 341

```text
CardTransaction <CardTx> contains the following CardEntry5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Card <Card> [0..1]  342
     PlainCardData <PlainCardData> [0..1]  343
       PAN <PAN> [1..1] Text 344
       CardSequenceNumber <CardSeqNb> [0..1] Text 344
       EffectiveDate <FctvDt> [0..1] YearMonth 344
       ExpiryDate <XpryDt> [1..1] YearMonth 344
       ServiceCode <SvcCd> [0..1] Text 344
       TrackData <TrckData> [0..*]  345
         TrackNumber <TrckNb> [0..1] Text 345
         TrackValue <TrckVal> [1..1] Text 345
       CardSecurityCode <CardSctyCd> [0..1]  345
         CSCManagement <CSCMgmt> [1..1] CodeSet 345
         CSCValue <CSCVal> [0..1] Text 346
     CardCountryCode <CardCtryCd> [0..1] Text 346
     CardBrand <CardBrnd> [0..1] ± 346
     AdditionalCardData <AddtlCardData> [0..1] Text 346
   POI <POI> [0..1]  346
     Identification <Id> [1..1] ± 347
     SystemName <SysNm> [0..1] Text 348
     GroupIdentification <GrpId> [0..1] Text 348
     Capabilities <Cpblties> [0..1]  348
       CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 348
       CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 349
       OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 349
       DisplayCapabilities <DispCpblties> [0..*]  350
         DisplayType <DispTp> [1..1] CodeSet 350
         NumberOfLines <NbOfLines> [1..1] Text 350
         LineWidth <LineWidth> [1..1] Text 350
       PrintLineWidth <PrtLineWidth> [0..1] Text 350
     Component <Cmpnt> [0..*]  350
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
341 March 2026
```

