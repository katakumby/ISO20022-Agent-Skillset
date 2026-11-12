---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.38 Safekeeping Place", "66.1.38.3 SafekeepingPlaceFormat28Choice", "66.1.38.3.3 TypeAndIdentification <TpAndId>", "66.1.38.3.3.1 SafekeepingPlaceType <SfkpgPlcTp>"]
file_pages: [5137]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.38.3.3.1 SafekeepingPlaceType <SfkpgPlcTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5137 to 5137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5137

```text
TypeAndIdentification <TpAndId> contains the following SafekeepingPlaceTypeAndIdentification1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 5137
   Identification <Id> [1..1] IdentifierSet C4 5137
66.1.38.3.3.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace1Code" on page 5358
CodeName Name Definition
CUST SharesHeldAtLocalCustodian Financial instruments held at a local
custodian.
ICSD SharesHeldAtICSD Financial instruments held at an
International Central Securities
Depository.
NCSD SharesHeldAtNCSD Financial instruments held at a National
Central Securities Depository.
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
66.1.38.3.3.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.38.3.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5137 May 2026
```

