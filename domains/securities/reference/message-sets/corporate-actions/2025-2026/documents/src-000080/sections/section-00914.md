---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.23 Safekeeping Place", "16.1.23.1 SafekeepingPlaceFormat42Choice", "16.1.23.1.4 TypeAndIdentification <TpAndId>", "16.1.23.1.4.1 SafekeepingPlaceType <SfkpgPlcTp>"]
file_pages: [1132]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.23.1.4.1 SafekeepingPlaceType <SfkpgPlcTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1132 to 1132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1132

```text
16.1.23.1.4.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: "SafekeepingPlace1Code" on page 1241
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
16.1.23.1.4.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by: C1 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 1244
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
16.1.23.1.5  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification78" on page 881 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 881
   Identification <Id> [0..1] Text 881
16.1.24 Securities Quantity
16.1.24.1  FinancialInstrumentQuantity18Choice
Definition: Choice between formats for the quantity of security.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1132 February 2026
```

