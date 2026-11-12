---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>", "3.4.10.1.22 ExDividendDate <ExDvddDt>"]
file_pages: [105]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1.22 ExDividendDate <ExDvddDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 105 to 105.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 105

```text
WhollyUnconditionalDate <WhlyUcondlDt> contains one of the following elements (see
"DateFormat30Choice" on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.22  ExDividendDate <ExDvddDt>
Presence: [0..1]
Definition: Date/time as from which trading (including exchange and OTC trading) occurs on the
underlying security without the benefit.
ExDividendDate <ExDvddDt> contains one of the following elements (see "DateFormat30Choice" on
page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 842
Or}   DateCode <DtCd> [1..1]  842
{Or     Code <Cd> [1..1] CodeSet 843
Or}     Proprietary <Prtry> [1..1] ± 843
3.4.10.1.23  OfficialAnnouncementPublicationDate <OffclAnncmntPblctnDt>
Presence: [0..1]
Definition: Date/time at which the corporate action is legally announced by an official body, for example,
publication by a governmental administration.
OfficialAnnouncementPublicationDate <OffclAnncmntPblctnDt> contains one of the following
elements (see "DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.24  SpecialExDate <SpclExDt>
Presence: [0..1]
Definition: Date/time from which 'special processing' can start to be used by participants for that event.
Special processing is a means of marking a transaction, that would normally be traded ex or cum, as
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 105 February 2026
```

