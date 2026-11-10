---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.6 TaxExemptionReason2Choice", "66.1.47.6.2 Proprietary <Prtry>"]
file_pages: [5254]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.6.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5254 to 5254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5254

```text
CodeName Name Definition
FORP OneOrBothForeign Account is for two account owners where
one or both are foreign.
ORDR Ordinary Ordinary reporting.
PENF PensionFund Account is for a pension fund for which a
tax exemption is permitted.
REFU Refugee Account is for a refugee or person
without a number assigned by a
government organisation, for example,
without a Danish Central Securities
Number.
RIHO RightsHolder Account is for a rights holder.
ADMI Administrator Administrator of the account is not the
owner.
TANR TwoNonResident Two or more of the account owners are
foreign residents.
OANR OneNonResident One of the account owners is a foreign
resident.
66.1.47.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Tax exemption reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.48 Transaction Type
66.1.48.1  TradeTransactionCondition8Choice
Definition: Choice of format for the trade transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5254
Or}   Proprietary <Prtry> [1..1] ± 5255
66.1.48.1.1  Code <Cd>
Presence: [1..1]
Definition: Trade condition expressed as a code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5254 May 2026
```

