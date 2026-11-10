---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.17 CardTransaction <CardTx>"]
file_pages: [80, 81]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.17 CardTransaction <CardTx>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 80 to 81.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

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
2.4.2.15.17  CardTransaction <CardTx>
Presence: [0..1]
Definition: Provides details of the card transaction included in the entry amount, when globalised by the
account servicer.
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
80 March 2026
```

## File page 81

```text
CardTransaction <CardTx> contains the following CardEntry5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Card <Card> [0..1]  82
     PlainCardData <PlainCardData> [0..1]  83
       PAN <PAN> [1..1] Text 84
       CardSequenceNumber <CardSeqNb> [0..1] Text 84
       EffectiveDate <FctvDt> [0..1] YearMonth 84
       ExpiryDate <XpryDt> [1..1] YearMonth 84
       ServiceCode <SvcCd> [0..1] Text 84
       TrackData <TrckData> [0..*]  85
         TrackNumber <TrckNb> [0..1] Text 85
         TrackValue <TrckVal> [1..1] Text 85
       CardSecurityCode <CardSctyCd> [0..1]  85
         CSCManagement <CSCMgmt> [1..1] CodeSet 85
         CSCValue <CSCVal> [0..1] Text 86
     CardCountryCode <CardCtryCd> [0..1] Text 86
     CardBrand <CardBrnd> [0..1] ± 86
     AdditionalCardData <AddtlCardData> [0..1] Text 86
   POI <POI> [0..1]  86
     Identification <Id> [1..1] ± 87
     SystemName <SysNm> [0..1] Text 88
     GroupIdentification <GrpId> [0..1] Text 88
     Capabilities <Cpblties> [0..1]  88
       CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 88
       CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 89
       OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 89
       DisplayCapabilities <DispCpblties> [0..*]  90
         DisplayType <DispTp> [1..1] CodeSet 90
         NumberOfLines <NbOfLines> [1..1] Text 90
         LineWidth <LineWidth> [1..1] Text 90
       PrintLineWidth <PrtLineWidth> [0..1] Text 90
     Component <Cmpnt> [0..*]  90
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
81 March 2026
```

