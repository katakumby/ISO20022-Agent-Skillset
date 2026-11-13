---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.3 Pagination1"]
file_pages: [889, 890]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.3 Pagination1

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 889 to 890.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 889

```text
AlternateClassification <AltrnClssfctn> contains the following elements (see
"GenericIdentification36" on page 878 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 878
   Issuer <Issr> [1..1] Text 878
   SchemeName <SchmeNm> [0..1] Text 879
16.1.15.3  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 889
   LastPageIndicator <LastPgInd> [1..1] Indicator 889
16.1.15.3.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: "Max5NumericText" on page 1251
16.1.15.3.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
16.1.15.4  AdditionalBusinessProcessFormat17Choice
Definition: Choice between a standard code or proprietary code to specify the type of the additional
business process.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 889
Or}   Proprietary <Prtry> [1..1] ± 891
16.1.15.4.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the additional business process linked to a corporate action event.
Datatype: "AdditionalBusinessProcess9Code" on page 1161
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 889 February 2026
```

## File page 890

```text
CodeName Name Definition
ACLA AutomaticMarketClaim Will automatically give rise to market
claims by the account servicer, for
example, a Central Securities Depository
(CSD).
ATXF SubjectToTransformation As a result of the corporate action, all
transactions in the underlying security
will be cancelled by the system and
replaced with transactions in the outturn
resource(s).
CNTR CancelUnderlyingTrades As a result of the corporate action, all
transactions in the underlying security
will be cancelled by the system.
NAMC NoAutomaticMarketClaimsAndTransformations Event will not automatically give rise to
market claims and transformations by
the account servicer, for example, a
Central Securities Depository (CSD).
NPLE NoSplitElection Issuer only allows a single option to be
selected per designated holding.
SCHM SchemeOrPlanOfArrangement Component event of a scheme/plan of
arrangement: a reorganisation of a
company or a group of companies, and
their capital.
CONS Consent Relates to a consent within a corporate
action event other than a Consent event
(: 22F:: CAEV//CONS).
PPUT PartialMandatoryPutRedemption Partial mandatory exchange of a portion
of bonds where the exchanged securities
are usually remarketed. The issuer may
offer holders the right to retain instead of
exchanging their securities. A lottery will
be used to determine eligibility for the
event.
FPRE FullPrefunding Full pre-funding of a debt instrument by
the issuer prior to original maturity when
the issuer deposits assets in trust.
Applicable only in the frame of a partial
defeasance corporate action event.
PPRE PartialPreFunding Partial pre-funding of a debt instrument
prior to maturity drawn through a lottery
process. One new security is issued with
an earlier maturity date for the refunded
(called portion) and the other new
security is issued with the original
maturity date for the non refunded
(remaining) portion. Applicable only in
the frame of a partial defeasance
corporate action event.
REAC RequiredAction Proceeds / entitlements of the
mandatory event can only be paid if
specified action is taken by the account
owner.
INCP IncentivePremiumPayment The event is a payment of an incentive
premium related to the voting conditions
prescribed at a general meeting.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 890 February 2026
```

