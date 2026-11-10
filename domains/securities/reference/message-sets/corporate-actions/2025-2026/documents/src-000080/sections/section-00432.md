---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.3 OptionFeatures <OptnFeatrs>", "8.4.12.3.1 Code <Cd>"]
file_pages: [583]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.3.1 Code <Cd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 583 to 583.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 583

```text
OptionFeatures <OptnFeatrs> contains one of the following OptionFeaturesFormat29Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 583
Or}   Proprietary <Prtry> [1..1] ± 583
8.4.12.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the features that may apply to a corporate action option.
Datatype: "OptionFeatures14Code" on page 1224
CodeName Name Definition
COND Conditional Feature whereby the holder can elect to
place a condition on the acceptance of
the option.
MAXC MaximumCash Maximum cash option, may be subject to
scaling, as such you may receive a
combination of cash and securities
outturn.
MAXS MaximumSecurities Maximum stock option, may be subject
to scaling, as such you may receive a
combination of securities and cash
outturn.
OPLF OddLotPreference Tender or exchange with the odd lot
preference.
PROR Proration Feature whereby the option can be
subject to pro ration in case, for
example, of over-subscription.
VVPR ReducedWithholdingTax Reduced withholding tax rate applies to
the option.
RGRS GrossDividendReinvestment Gross dividend is reinvested.
RNET NetDividendReinvestment Dividend reinvestment is processed net
of withholding tax.
8.4.12.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the features that may apply to a corporate action option.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 583 February 2026
```

