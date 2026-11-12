---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["65 reda.049.001.01 AccountLinkCreationRequestV01", "65.4 Message Building Blocks", "65.4.2 AccountLink <AcctLk>", "65.4.2.4 ValidFrom <VldFr>"]
file_pages: [2373]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 65.4.2.4 ValidFrom <VldFr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2373 to 2373.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2373

```text
CashAccount <CshAcct> contains the following elements (see "CashAccount38" on page 2828 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2828
   Type <Tp> [0..1] ± 2828
   Currency <Ccy> [0..1] CodeSet C1 2828
   Name <Nm> [0..1] Text 2829
   Proxy <Prxy> [0..1] ± 2829
65.4.2.4  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the securities account is linked to the cash account.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
65.4.2.5  ValidTo <VldTo>
Presence: [0..1]
Definition: Defines the date until when the securities account is linked to the cash account.
ValidTo <VldTo> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
65.4.2.6  DefaultIndicator <DfltInd>
Presence: [1..1]
Definition: Specifies whether created account link is set as default for settlement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
65.4.2.7  CollateralisationIndicator <CollstnInd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities 2373 August 2026
```

