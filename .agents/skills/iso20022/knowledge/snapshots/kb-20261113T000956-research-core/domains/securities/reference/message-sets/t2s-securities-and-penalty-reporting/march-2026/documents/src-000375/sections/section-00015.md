---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks"]
file_pages: [20, 21, 22, 23, 24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
preceding_topic_continuations: [{"constraint_ids": ["C13", "C14", "C15", "C16"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 20, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-securities-and-penalty-reporting/march-2026/documents/src-000375/sections/section-00014.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 20 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 20, C13–C16 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00014.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 20

```text
C13 Party3PresenceRule
If Party3 is present, then Party2 must be present.
C14 Party4PresenceRule
If Party4 is present, then Party3 must be present.
C15 Party5PresenceRule
If Party5 is present, then Party4 must be present.
C16 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 QueryDefinition <QryDef>
Presence: [1..1]
Definition: Defines the securities settlement instruction query criteria.
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 20 March 2026
```

## File page 21

```text
QueryDefinition <QryDef> contains the following SettlementInstructionQueryDefinition4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [1..1] CodeSet 25
   SearchCriteria <SchCrit> [1..1]  26
     References <Refs> [0..*]  31
{Or       AccountOwnerTransactionIdentification
<AcctOwnrTxId>
[1..1] Text 32
Or       AccountServicerTransactionIdentification
<AcctSvcrTxId>
[1..1] Text 32
Or       MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 32
Or       CounterpartyMarketInfrastructureTransactionIdenti
fication <CtrPtyMktInfrstrctrTxId>
[0..1] Text 32
Or       ProcessorTransactionIdentification <PrcrTxId> [1..1] Text 32
Or       PoolIdentification <PoolId> [1..1] Text 33
Or       CommonIdentification <CmonId> [1..1] Text 33
Or       TradeIdentification <TradId> [1..1] Text 33
Or}       CorporateActionEventIdentification
<CorpActnEvtId>
[1..1] Text 33
     Status <Sts> [0..*]  33
       Type <Tp> [1..1]  34
         ProcessingStatus <PrcgSts> [0..*] ± 35
         InferredMatchingStatus <IfrrdMtchgSts> [0..*] ± 35
         MatchingStatus <MtchgSts> [0..*] ± 35
         SettlementStatus <SttlmSts> [0..*] ± 35
         Settled <Sttld> [0..1] ± C3 36
       DatePeriod <DtPrd> [0..1]  36
{Or         Date <Dt> [1..1]  36
{Or           FromDate <FrDt> [1..1] Date 37
Or           ToDate <ToDt> [1..1] Date 37
Or           FromToDate <FrToDt> [1..1] ± 37
Or           EqualDate <EQDt> [1..1] Date 37
Or}           NotEqualDate <NEQDt> [1..1] Date 37
Or}         DateTime <DtTm> [1..1]  37
{Or           FromDateTime <FrDtTm> [1..1] DateTime 38
Or           ToDateTime <ToDtTm> [1..1] DateTime 38
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 21 March 2026
```

## File page 22

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           FromToDateTime <FrToDtTm> [1..1] ± 38
Or           EqualDateTime <EQDtTm> [1..1] DateTime 38
Or}           NotEqualDateTime <NEQDtTm> [1..1] DateTime 38
     SecuritiesMovementType <SctiesMvmntTp> [0..*] CodeSet 38
     Payment <Pmt> [0..*] CodeSet 39
     SecuritiesTransactionType <SctiesTxTp> [0..*] ± 39
     FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C9, C10,
C11
39
     Priority <Prty> [0..*] ± 40
     SafekeepingAccount <SfkpgAcct> [0..*] ± 41
     CashAccount <CshAcct> [0..*]  41
{Or       Equal <EQ> [1..1] ± 41
Or       ContainText <CTTxt> [1..1] Text 42
Or}       NotContainText <NCTTxt> [1..1] Text 42
     TradeDate <TradDt> [0..1]  42
{Or       Date <Dt> [1..1]  42
{Or         FromDate <FrDt> [1..1] Date 43
Or         ToDate <ToDt> [1..1] Date 43
Or         FromToDate <FrToDt> [1..1] ± 43
Or         EqualDate <EQDt> [1..1] Date 43
Or}         NotEqualDate <NEQDt> [1..1] Date 43
Or}       DateTime <DtTm> [1..1]  43
{Or         FromDateTime <FrDtTm> [1..1] DateTime 44
Or         ToDateTime <ToDtTm> [1..1] DateTime 44
Or         FromToDateTime <FrToDtTm> [1..1] ± 44
Or         EqualDateTime <EQDtTm> [1..1] DateTime 44
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 44
     SettlementQuantity <SttlmQty> [0..1]  44
{Or       Quantity <Qty> [1..1]  45
{Or         Unit <Unit> [1..1]  46
{Or           FromQuantity <FrQty> [1..1]  47
             Boundary <Bdry> [1..1] Quantity 47
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 22 March 2026
```

## File page 23

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             Included <Incl> [1..1] Indicator 47
Or           ToQuantity <ToQty> [1..1]  48
             Boundary <Bdry> [1..1] Quantity 48
             Included <Incl> [1..1] Indicator 48
Or           FromToQuantity <FrToQty> [1..1]  48
             FromQuantity <FrQty> [1..1]  48
               Boundary <Bdry> [1..1] Quantity 49
               Included <Incl> [1..1] Indicator 49
             ToQuantity <ToQty> [1..1]  49
               Boundary <Bdry> [1..1] Quantity 49
               Included <Incl> [1..1] Indicator 49
Or           EqualQuantity <EQQty> [1..1] Quantity 50
Or}           NotEqualQuantity <NEQQty> [1..1] Quantity 50
Or         FaceAmount <FaceAmt> [1..1] ± 50
Or}         AmortisedValue <AmtsdVal> [1..1] ± 50
Or}       OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  51
         FaceAmount <FaceAmt> [1..1] ± 51
         AmortisedValue <AmtsdVal> [1..1] ± 52
     SettledQuantity <SttldQty> [0..1]  52
{Or       Quantity <Qty> [1..1]  53
{Or         Unit <Unit> [1..1]  54
{Or           FromQuantity <FrQty> [1..1]  55
             Boundary <Bdry> [1..1] Quantity 55
             Included <Incl> [1..1] Indicator 55
Or           ToQuantity <ToQty> [1..1]  56
             Boundary <Bdry> [1..1] Quantity 56
             Included <Incl> [1..1] Indicator 56
Or           FromToQuantity <FrToQty> [1..1]  56
             FromQuantity <FrQty> [1..1]  56
               Boundary <Bdry> [1..1] Quantity 57
               Included <Incl> [1..1] Indicator 57
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 23 March 2026
```

## File page 24

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
             ToQuantity <ToQty> [1..1]  57
               Boundary <Bdry> [1..1] Quantity 57
               Included <Incl> [1..1] Indicator 57
Or           EqualQuantity <EQQty> [1..1] Quantity 58
Or}           NotEqualQuantity <NEQQty> [1..1] Quantity 58
Or         FaceAmount <FaceAmt> [1..1] ± 58
Or}         AmortisedValue <AmtsdVal> [1..1] ± 58
Or}       OriginalAndCurrentFace <OrgnlAndCurFace> [1..1]  59
         FaceAmount <FaceAmt> [1..1] ± 59
         AmortisedValue <AmtsdVal> [1..1] ± 60
     SettlementAmount <SttlmAmt> [0..1] ± 60
     SettledAmount <SttldAmt> [0..1] ± 60
     IntendedSettlementDate <IntnddSttlmDt> [0..1]  61
{Or       Date <Dt> [1..1]  61
{Or         FromDate <FrDt> [1..1] Date 61
Or         ToDate <ToDt> [1..1] Date 62
Or         FromToDate <FrToDt> [1..1] ± 62
Or         EqualDate <EQDt> [1..1] Date 62
Or}         NotEqualDate <NEQDt> [1..1] Date 62
Or}       DateTime <DtTm> [1..1]  62
{Or         FromDateTime <FrDtTm> [1..1] DateTime 62
Or         ToDateTime <ToDtTm> [1..1] DateTime 63
Or         FromToDateTime <FrToDtTm> [1..1] ± 63
Or         EqualDateTime <EQDtTm> [1..1] DateTime 63
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 63
     EffectiveSettlementDate <FctvSttlmDt> [0..1]  63
{Or       Date <Dt> [1..1]  64
{Or         FromDate <FrDt> [1..1] Date 64
Or         ToDate <ToDt> [1..1] Date 64
Or         FromToDate <FrToDt> [1..1] ± 65
Or         EqualDate <EQDt> [1..1] Date 65
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 24 March 2026
```

