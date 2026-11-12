---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.4 Message Building Blocks", "2.4.1 MessageHeader <MsgHdr>"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.4.1 MessageHeader <MsgHdr>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
2.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 68 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 68
   CreationDateTime <CreDtTm> [0..1] DateTime 68
2.4.2 CollateralValue <CollVal>
Presence: [1..*]
Definition: Represents the valuation of securities positions for auto-collateralisation.
CollateralValue <CollVal> contains the following CollateralValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..1] ± C7, C8,
C9, C10,
C11
10
   ValuationDate <ValtnDt> [1..1] Date 11
   ValuationCurrency <ValtnCcy> [0..1] CodeSet C1 11
   ValuationPrice <ValtnPric> [1..1]  11
{Or     Amount <Amt> [1..1] Amount 11
Or     AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 11
Or}     Coefficient <Coeff> [1..1] Quantity 12
   ValuationCloseLinkPrice <ValtnClsLkPric> [0..1]  12
{Or     Amount <Amt> [1..1] Amount 12
Or     AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 12
Or}     Coefficient <Coeff> [1..1] Quantity 13
   CleanPrice <CleanPric> [0..1] ± 13
   AccruedInterest <AcrdIntrst> [0..1] ± 13
   Haircut <Hrcut> [0..1] Rate 13
   CloseLinkHaircut <ClsLkHrcut> [0..1] Rate 14
   PoolFactor <PoolFctr> [0..1] Rate 14
   ForeignExchange <FX> [0..1] ± 14
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 9 May 2025
```

