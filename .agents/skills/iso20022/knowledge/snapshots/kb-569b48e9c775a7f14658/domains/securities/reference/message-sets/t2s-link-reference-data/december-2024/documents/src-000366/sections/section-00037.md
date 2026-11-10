---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["5 reda.049.001.01 AccountLinkCreationRequestV01", "5.4 Message Building Blocks", "5.4.2 AccountLink <AcctLk>", "5.4.2.4 ValidFrom <VldFr>"]
file_pages: [39]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.049.001.01"]
---

# 5.4.2.4 ValidFrom <VldFr>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 39 to 39.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
CashAccount <CshAcct> contains the following elements (see "CashAccount38" on page 55 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 55
   Type <Tp> [0..1] ± 55
   Currency <Ccy> [0..1] CodeSet C1 55
   Name <Nm> [0..1] Text 56
   Proxy <Prxy> [0..1] ± 56
5.4.2.4  ValidFrom <VldFr>
Presence: [1..1]
Definition: Defines the date since when the securities account is linked to the cash account.
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
5.4.2.5  ValidTo <VldTo>
Presence: [0..1]
Definition: Defines the date until when the securities account is linked to the cash account.
ValidTo <VldTo> contains one of the following elements (see "DateAndDateTime2Choice" on
page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
5.4.2.6  DefaultIndicator <DfltInd>
Presence: [1..1]
Definition: Specifies whether created account link is set as default for settlement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 77):
• Meaning When True: Yes
• Meaning When False: No
5.4.2.7  CollateralisationIndicator <CollstnInd>
Presence: [1..1]
Approved by the Securities SEG on 21 November 2024. reda.049.001.01 AccountLinkCreationRequestV01
Target2-Securities - Link Reference Data 39 December 2024
```

