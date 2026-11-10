---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.1 DateDetails <DtDtls>", "3.4.10.1.1 AnnouncementDate <AnncmntDt>"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.1.1 AnnouncementDate <AnncmntDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ThirdPartyDeadline <ThrdPtyDdln> [0..1] ± 107
   EarlyThirdPartyDeadline <EarlyThrdPtyDdln> [0..1] ± 108
   MarketClaimTrackingEndDate <MktClmTrckgEndDt> [0..1] ± 108
   LeadPlaintiffDeadline <LeadPlntffDdln> [0..1] ± 108
   FilingDate <FilgDt> [0..1] ± 109
   HearingDate <HrgDt> [0..1] ± 109
Constraints
• EffectiveDateRule
Effective date is to be used in events where there is no concept of entitlement, for example Name
Change (CHAN) or Place of Incorporation (PLAC), and in events where there is a sense of eligibility
but with a legal obligation, for example Merger (MRGR).
3.4.10.1.1  AnnouncementDate <AnncmntDt>
Presence: [0..1]
Definition: Date/time at which the issuer announced that a corporate action event will occur.
AnnouncementDate <AnncmntDt> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
3.4.10.1.2  CertificationDeadline <CertfctnDdln>
Presence: [0..1]
Definition: Deadline by which the certification must be sent.
CertificationDeadline <CertfctnDdln> contains one of the following elements (see
"DateFormat43Choice" on page 843 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 843
Or}   DateCode <DtCd> [1..1]  844
{Or     Code <Cd> [1..1] CodeSet 844
Or}     Proprietary <Prtry> [1..1] ± 844
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 98 February 2026
```

