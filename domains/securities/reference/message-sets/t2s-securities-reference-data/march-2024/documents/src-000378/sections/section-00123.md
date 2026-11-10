---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.6 OptionStyle <OptnStyle>"]
file_pages: [181]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.6 OptionStyle <OptnStyle>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 181 to 181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 181

```text
13.1.2.2.2.6  OptionStyle <OptnStyle>
Presence: [0..1]
Definition: Specifies how an option can be exercised (American, European, Bermudan).
OptionStyle <OptnStyle> contains one of the following OptionStyle1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 181
Or}   Proprietary <Prtry> [1..1] ± 181
13.1.2.2.2.6.1  Code <Cd>
Presence: [1..1]
Definition: Option style is defined using a code.
Datatype: "OptionStyle1Code" on page 520
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
ASIA Asian Option where the payoff is not
determined by the underlying price at
maturity but by the average underlying
price over some pre-set period of time.
CANA Canary Option whose exercise style lies
somewhere between European options
and Bermudan options. The holder can
exercise the option at quarterly dates,
but not before a set time period (typically
one year) has elapsed.
13.1.2.2.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option style is defined using a data source scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 480 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 480
   SchemeName <SchmeNm> [0..1] Text 480
   Issuer <Issr> [1..1] Text 481
13.1.2.2.2.7  OptionType <OptnTp>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 181 March 2024
```

