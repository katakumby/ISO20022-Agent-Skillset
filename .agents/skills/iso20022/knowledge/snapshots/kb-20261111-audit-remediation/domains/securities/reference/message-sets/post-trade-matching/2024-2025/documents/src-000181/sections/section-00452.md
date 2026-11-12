---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.24 Rating", "7.1.24.1 Rating1", "7.1.24.1.1 RatingScheme <RatgSchme>"]
file_pages: [518]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.24.1.1 RatingScheme <RatgSchme>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 518 to 518.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 518

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RatingScheme <RatgSchme> [1..1] Text 518
   ValueDate <ValDt> [1..1] DateTime 518
   ValueIdentification <ValId> [1..1] IdentifierSet 518
7.1.24.1.1  RatingScheme <RatgSchme>
Presence: [1..1]
Definition: Information regarding the entity that assigns the rating.
Datatype: "Max35Text" on page 669
7.1.24.1.2  ValueDate <ValDt>
Presence: [1..1]
Definition: Date/time as from which the rating is valid.
Datatype: "ISODateTime" on page 662
7.1.24.1.3  ValueIdentification <ValId>
Presence: [1..1]
Definition: Specifies the rating, which has been assigned to a security by a rating agency.
Datatype: "RatingValueIdentifier" on page 665
7.1.25 Securities Quantity
7.1.25.1  FinancialInstrumentQuantity18Choice
Definition: Choice between formats for the quantity of security.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 518
Or}   FaceAmount <FaceAmt> [1..1] Amount 518
7.1.25.1.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, for example, a number of shares.
Datatype: "DecimalNumber" on page 666
7.1.25.1.2  FaceAmount <FaceAmt>
Presence: [1..1]
Definition: Quantity expressed as an amount representing the face amount, that is, the principal, of a
debt instrument.
Datatype: "ImpliedCurrencyAndAmount" on page 613
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 518 February 2025
```

