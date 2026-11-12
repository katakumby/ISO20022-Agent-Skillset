---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.37 SafekeepingPlaceFormat29Choice", "7.1.18.37.3 TypeAndIdentification <TpAndId>", "7.1.18.37.3.2 Identification <Id>"]
file_pages: [400]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.37.3.2 Identification <Id>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 400 to 400.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 400

```text
7.1.18.37.3.2  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 551
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.18.37.4  Proprietary <Prtry>
Presence: [1..1]
Definition: Place of safekeeping expressed with a propriety identification scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification78" on page 353 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 353
   Identification <Id> [0..1] Text 353
7.1.18.38  Registration9Choice
Definition: Choice of format for the registration information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 400
Or}   Proprietary <Prtry> [1..1] ± 401
7.1.18.38.1  Code <Cd>
Presence: [1..1]
Definition: Registration information expressed as an ISO 20022 code.
Datatype: "Registration1Code" on page 526
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 400 March 2026
```

