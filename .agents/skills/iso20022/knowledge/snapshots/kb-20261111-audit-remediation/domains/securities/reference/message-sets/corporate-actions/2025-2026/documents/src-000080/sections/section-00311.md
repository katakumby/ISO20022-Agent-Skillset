---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.4 OfferType <OfferTp>", "7.4.13.4.1 Code <Cd>"]
file_pages: [431]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.4.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 431 to 431.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 431

```text
7.4.13.4.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the conditions that apply to the offer.
Datatype: "OfferType6Code" on page 0
CodeName Name Definition
DISS DissenterRights Securities holder has the right to
disagree with a mandatory event. This
right is not inherent in all offers and
therefore must be noted in
announcements only when applicable.
ERUN RestrictionExchange Exchange of Restricted to Unrestricted
(or vice versa).
FINL FinalOffer Final or last offer to holders subject to
offer conditions being reached, for
example, 50 percent accepted on a
tender.
PART PartialOffer Offer made by the offeror for a portion of
the outstanding shares not already
owned by the offeror.
SQUE SqueezeOutBid Offer launched by a company, in
possession of a large number of the
shares (90% - 95%) of a company
(generally as a result of a tender offer),
in order to acquire the remaining shares
of that company.
NDIS DissenterRightsNotApplicable Dissenter's rights are not applicable for
this option of the offer.
7.4.13.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the conditions that apply to the offer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
7.4.13.5  OptionFeatures <OptnFeatrs>
Presence: [0..*]
Definition: Specifies the features that may apply to a corporate action option.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 431 February 2026
```

