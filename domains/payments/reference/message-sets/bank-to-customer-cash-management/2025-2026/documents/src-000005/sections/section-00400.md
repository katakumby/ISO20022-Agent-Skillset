---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>"]
file_pages: [598, 599]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17 CardTransaction <CardTx>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 598 to 599.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 598

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
4.4.2.14.17  CardTransaction <CardTx>
Presence: [0..1]
Definition: Provides details of the card transaction included in the entry amount, when globalised by the
account servicer.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
598 March 2026
```

## File page 599

```text
CardTransaction <CardTx> contains the following CardEntry5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Card <Card> [0..1]  600
     PlainCardData <PlainCardData> [0..1]  601
       PAN <PAN> [1..1] Text 602
       CardSequenceNumber <CardSeqNb> [0..1] Text 602
       EffectiveDate <FctvDt> [0..1] YearMonth 602
       ExpiryDate <XpryDt> [1..1] YearMonth 602
       ServiceCode <SvcCd> [0..1] Text 602
       TrackData <TrckData> [0..*]  603
         TrackNumber <TrckNb> [0..1] Text 603
         TrackValue <TrckVal> [1..1] Text 603
       CardSecurityCode <CardSctyCd> [0..1]  603
         CSCManagement <CSCMgmt> [1..1] CodeSet 603
         CSCValue <CSCVal> [0..1] Text 604
     CardCountryCode <CardCtryCd> [0..1] Text 604
     CardBrand <CardBrnd> [0..1] ± 604
     AdditionalCardData <AddtlCardData> [0..1] Text 604
   POI <POI> [0..1]  604
     Identification <Id> [1..1] ± 605
     SystemName <SysNm> [0..1] Text 606
     GroupIdentification <GrpId> [0..1] Text 606
     Capabilities <Cpblties> [0..1]  606
       CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 606
       CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 607
       OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 607
       DisplayCapabilities <DispCpblties> [0..*]  608
         DisplayType <DispTp> [1..1] CodeSet 608
         NumberOfLines <NbOfLines> [1..1] Text 608
         LineWidth <LineWidth> [1..1] Text 608
       PrintLineWidth <PrtLineWidth> [0..1] Text 608
     Component <Cmpnt> [0..*]  608
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
599 March 2026
```

