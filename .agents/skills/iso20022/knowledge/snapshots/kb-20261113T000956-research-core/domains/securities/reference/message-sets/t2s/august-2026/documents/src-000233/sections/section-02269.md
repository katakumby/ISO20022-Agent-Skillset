---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.57 Registration9Choice", "82.1.19.57.1 Code <Cd>"]
file_pages: [3044]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.57.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3044 to 3044.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3044

```text
82.1.19.57.1  Code <Cd>
Presence: [1..1]
Definition: Registration information expressed as an ISO 20022 code.
Datatype: "Registration1Code" on page 3283
CodeName Name Definition
NREG StreetName Hold the securities in street name. If
there is a standing instruction in place to
register on receipt, then this standing
instruction is to be ignored.
YREG Registered Register on receipt. If there is a standing
instruction in place to hold the securities
in street name, then this standing
instruction is to be ignored.
82.1.19.57.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Registration information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.58  MarketInfrastructureIdentification1Choice
Definition: Specifies the market infrastructure identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3044
Or}   Proprietary <Prtry> [1..1] Text 3044
82.1.19.58.1  Code <Cd>
Presence: [1..1]
Definition: Infrastructure through which the payment instruction is processed, as published in an
external clearing system identification code list.
Datatype: "ExternalMarketInfrastructure1Code" on page 3242
82.1.19.58.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Clearing system identification in a proprietary form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3044 August 2026
```

