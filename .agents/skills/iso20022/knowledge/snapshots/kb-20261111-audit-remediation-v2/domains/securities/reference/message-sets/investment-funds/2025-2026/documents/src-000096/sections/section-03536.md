---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.29 ProcessingCharacteristics12", "66.1.26.29.2 RedemptionAuthorisation <RedAuthstn>"]
file_pages: [4786]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.29.2 RedemptionAuthorisation <RedAuthstn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4786 to 4786.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4786

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.26.29.2  RedemptionAuthorisation <RedAuthstn>
Presence: [0..1]
Definition: Specifies whether an application form is required for a redemption.
RedemptionAuthorisation <RedAuthstn> contains the following Forms1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ApplicationForm <ApplForm> [1..1] Indicator 4786
   SignatureType <SgntrTp> [1..1] CodeSet 4786
66.1.26.29.2.1  ApplicationForm <ApplForm>
Presence: [1..1]
Definition: Indicates whether a physical application form is required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.29.2.2  SignatureType <SgntrTp>
Presence: [1..1]
Definition: Type of signature.
Datatype: "SignatureType1Code" on page 5363
CodeName Name Definition
ORIG Original The investor's written signature is
required. Can also be known as physical
or wet signature.
DIGI Digital A technical signature that includes
algorithms and private key and public
key information. Used to sign and verify
the contents of a message.
ELEC Electronic A copy of a physical or original signature
in an electronic format.
NONE None There is no signature required in any
form.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4786 May 2026
```

