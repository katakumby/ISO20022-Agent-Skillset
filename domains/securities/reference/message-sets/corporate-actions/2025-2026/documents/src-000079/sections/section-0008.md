---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000079"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["Scope and Functionality", "Background"]
content_origin: "source-transcription"
---

# Background

Source: [src-000079](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart1_CorporateActions_2025_2026_v2.docx). Locator: heading path Scope and Functionality / Background.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P80** Background

**P81** This Message Definition Report covers the latest version of the set of thirteen ISO 20022 message definitions developed by SWIFT in close collaboration with the ISO15022/ISO20022 community of users and approved by the Securities Standards Evaluation Group (SEG) on 27th January 2026.

**P82** Most of these ISO 20022 message definitions were reverse engineered from ISO 15022 messages.

**P83** These messages were specifically designed to support most of the corporate actions related business processes through the full corporate action chain of business actors and are meant to cover the whole corporate action events lifecycle.

**P84** The ISO 15022 and ISO 20022 standards will coexist for a number of years. Until this coexistence period ends the usage of certain data types is restricted, to ensure full interoperability between ISO 15022 and ISO 20022 users. These restrictions, which are described by textual usage rules in the ISO 20022 message, have been implemented directly in the message schema. This set of messages will be used by intermediaries involved in the corporate actions processing chain, for example, investment managers, global custodians, stock exchanges and market infrastructures.

**P85** Historical background

**P86** With harmonisation industry initiatives such as Giovannini, there is an increasing pressure on the securities industry to change from proprietary standards to ISO standards.

**P87** SWIFT was requested by its community to develop ISO 20022 messages equivalent to ISO 15022 to allow ISO 'newcomers' to directly adopt ISO 20022. To limit the impact on existing ISO 15022 users, the ISO 20022 messages were directly reverse-engineered from ISO 15022 messages.

**P88** In this process, SWIFT made sure to:

**P89** design the ISO 20022 messages with mapping to ISO 15022 in mind to ensure the same levels of STP as today,

**P90** limit the ISO 20022 functionality to the functionality available in ISO 15022 during the coexistence period. That is, it would not be possible to do something with an ISO 20022 message that could not be done in its equivalent ISO 15022 messages and vice versa,

**P91** synchronise the maintenance between the two standards in terms of timing, review process and content,

**P92** provide coexistence support, for example, the necessary mapping or translation documentation.

**P93** In addition to the above, SWIFT undertook the following tasks to ensure that the right balance was kept between the need for close reverse engineering from ISO 15022 and the need for leveraging the benefits and principles of ISO 20022:

**P94** ensure that global market practices defined by the Securities Market Practice Group (SMPG) were adhered to during the process,

**P95** solve ISO 15022 standards issues that were identified by the ISO 15022 Registration Authority and the SMPG and that had been postponed awaiting equivalent ISO 20022 messages,

**P96** ensure that additional requirements identified by harmonisation initiatives such as Giovannini were included, in both ISO 15022 and ISO 20022 unless agreed otherwise,

**P97** design the financial instruments identification and attributes based upon the Financial Instrument Business Information Model (FIBIM) as defined by ISO TC 68 SC 4 WG 11. Please see the ISO web site page for more information on this topic: http://www.iso.org/iso/standards_development/technical_committees/list_of_iso_technical_committees/iso_technical_committee.htm?commid=49690

