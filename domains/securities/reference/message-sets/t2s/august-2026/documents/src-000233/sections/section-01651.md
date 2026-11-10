---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.11 Restriction <Rstrctn>", "58.4.2.2.2.11.2 New <New>", "58.4.2.2.2.11.2.1 RestrictionType <RstrctnTp>"]
file_pages: [2285]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.11.2.1 RestrictionType <RstrctnTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2285 to 2285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2285

```text
New <New> contains the following Restriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RestrictionType <RstrctnTp> [1..1]  2285
{Or     Code <Cd> [1..1] Text 2285
Or}     Proprietary <Prtry> [1..1] ± 2285
   ValidFrom <VldFr> [1..1] DateTime 2285
   ValidUntil <VldUntil> [0..1] DateTime 2286
58.4.2.2.2.11.2.1  RestrictionType <RstrctnTp>
Presence: [1..1]
Definition: Type of the restriction.
RestrictionType <RstrctnTp> contains one of the following CodeOrProprietary1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] Text 2285
Or}   Proprietary <Prtry> [1..1] ± 2285
58.4.2.2.2.11.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Element expressed as an ISO 20022 code from an external list.
Datatype: "Max4Text" on page 3329
58.4.2.2.2.11.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Element expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2969
   SchemeName <SchmeNm> [0..1] Text 2969
   Issuer <Issr> [1..1] Text 2969
58.4.2.2.2.11.2.2  ValidFrom <VldFr>
Presence: [1..1]
Definition: Date from when the restriction is valid.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2285 August 2026
```

