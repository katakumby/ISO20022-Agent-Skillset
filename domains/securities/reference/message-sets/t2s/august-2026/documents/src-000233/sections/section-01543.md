---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.4 Message Building Blocks", "44.4.1 MessageHeader <MsgHdr>"]
file_pages: [2166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.4.1 MessageHeader <MsgHdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2166 to 2166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2166

```text
44.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 2982 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2982
   CreationDateTime <CreDtTm> [0..1] DateTime 2982
44.4.2 CollateralValue <CollVal>
Presence: [1..*]
Definition: Represents the valuation of securities positions for auto-collateralisation.
CollateralValue <CollVal> contains the following CollateralValue5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecurityIdentification <SctyId> [1..1] ± C7, C8,
C9, C10,
C11
2167
   ValuationDate <ValtnDt> [1..1] Date 2168
   ValuationCurrency <ValtnCcy> [0..1] CodeSet C1 2168
   ValuationPrice <ValtnPric> [1..1]  2168
{Or     Amount <Amt> [1..1] Amount 2168
Or     AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 2168
Or}     Coefficient <Coeff> [1..1] Quantity 2169
   ValuationCloseLinkPrice <ValtnClsLkPric> [0..1]  2169
{Or     Amount <Amt> [1..1] Amount 2169
Or     AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 2169
Or}     Coefficient <Coeff> [1..1] Quantity 2170
   CleanPrice <CleanPric> [0..1] ± 2170
   AccruedInterest <AcrdIntrst> [0..1] ± 2170
   Haircut <Hrcut> [0..1] Rate 2170
   CloseLinkHaircut <ClsLkHrcut> [0..1] Rate 2171
   PoolFactor <PoolFctr> [0..1] Rate 2171
   ForeignExchange <FX> [0..1] ± 2171
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2166 August 2026
```

